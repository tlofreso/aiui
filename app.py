# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "quart",
#     "claude-agent-sdk>=0.1.6",
# ]
# ///

import json
import os
import uuid
from pathlib import Path

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    SystemMessage,
    TextBlock,
)
from quart import Quart, jsonify, render_template, request

app = Quart(__name__)
messages = []
session_id = None

SCHEMA_PATH = Path(__file__).parent / "schema.json"
SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.md"

with open(SCHEMA_PATH) as f:
    CHAT_RESPONSE_SCHEMA = json.load(f)

with open(SYSTEM_PROMPT_PATH) as f:
    SYSTEM_PROMPT = f.read()


async def get_claude_response(user_message: str) -> dict[str, str]:
    """Get response from Claude SDK with structured output (message and html fields)."""
    global session_id

    options = ClaudeAgentOptions(
        cwd=os.getcwd(),
        setting_sources=["project"],
        allowed_tools=["Skill", "Read"],
        output_format=CHAT_RESPONSE_SCHEMA,
        system_prompt=SYSTEM_PROMPT,
        resume=session_id,
    )

    response_data = {"message": "", "html": ""}
    fallback_text = ""

    try:
        async with ClaudeSDKClient(options) as client:
            await client.query(user_message)

            async for msg in client.receive_response():
                if isinstance(msg, SystemMessage):
                    # Capture session ID from init message
                    if msg.subtype == "init" and "session_id" in msg.data:
                        session_id = msg.data["session_id"]
                        print(f"[DEBUG] Session ID: {session_id}")
                elif isinstance(msg, ResultMessage):
                    # Check for structured output in ResultMessage
                    if hasattr(msg, "structured_output") and msg.structured_output:
                        response_data = msg.structured_output
                        print(f"[DEBUG] Structured output received: {response_data}")
                    else:
                        print(f"[DEBUG] ResultMessage but no structured_output")
                elif isinstance(msg, AssistantMessage):
                    # Fallback: collect text blocks from assistant messages
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            fallback_text += block.text + " "
                            print(f"[DEBUG] AssistantMessage text: {block.text[:100]}...")

        # If no structured output was received, use fallback text
        if (
            not response_data.get("message")
            and not response_data.get("html")
            and fallback_text
        ):
            response_data = {"message": fallback_text.strip(), "html": ""}
            print(f"[DEBUG] Using fallback text")

        print(f"[DEBUG] Final response_data: {response_data}")

        # Ensure we always return something valid
        if not response_data.get("message") and not response_data.get("html"):
            print("[WARNING] Empty response detected, returning default message")
            response_data = {
                "message": "I apologize, but I encountered an issue generating a response. Could you please try again?",
                "html": ""
            }

        return response_data

    except Exception as e:
        print(f"[ERROR] Exception in get_claude_response: {e}")
        import traceback
        traceback.print_exc()
        return {
            "message": f"Sorry, I encountered an error: {str(e)}",
            "html": ""
        }


def create_messages_from_response(response: dict[str, str]) -> list:
    """
    Convert Claude's response into message objects.
    The response is a dict with 'message' and 'html' fields.
    Returns a list of message dicts to be added to the messages array.
    """
    new_messages = []

    # Get message and html from structured output
    text_part = response.get("message", "").strip()
    html_part = response.get("html", "").strip()

    # Add text message if present
    if text_part:
        new_messages.append({"chat_type": "start", "content": text_part})

    # Add card if present
    if html_part:
        card_id = str(uuid.uuid4())
        new_messages.append(
            {
                "chat_type": "start",
                "message_type": "card",
                "card_id": card_id,
                "html": html_part,
                "content": "",
                "card_submitted": False,
            }
        )

    return new_messages


@app.route("/")
async def index():
    """Render the chat interface."""
    return await render_template("chat.html", page_title="AI Chat", messages=messages)


@app.route("/api/send_message", methods=["POST"])
async def send_message():
    """Handle incoming chat messages."""
    try:
        data = await request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify(
                {"status": "error", "message": "Message cannot be empty"}
            ), 400

        messages.append({"chat_type": "end", "content": user_message})
        claude_response = await get_claude_response(user_message)
        new_messages = create_messages_from_response(claude_response)
        messages.extend(new_messages)

        return jsonify(
            {
                "status": "success",
                "responses": new_messages,  # Return array of messages
            }
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/card_action", methods=["POST"])
async def card_action():
    """Handle card interaction submissions."""
    try:
        data = await request.get_json()
        card_id = data.get("card_id")
        action = data.get("action")
        form_data = data.get("data", {})

        print(f"[DEBUG] Card action received - card_id: {card_id}, action: {action}, data: {form_data}")

        if not card_id or not action:
            return jsonify(
                {"status": "error", "message": "card_id and action are required"}
            ), 400

        # Find the card in messages and mark as submitted
        card_found = False
        card_type = None
        for msg in messages:
            if msg.get("card_id") == card_id:
                msg["card_submitted"] = True
                # Try to extract card_type from HTML if present
                html = msg.get("html", "")
                if "data-card-type=" in html:
                    start = html.find('data-card-type="') + len('data-card-type="')
                    end = html.find('"', start)
                    card_type = html[start:end] if end > start else "unknown"
                card_found = True
                break

        if not card_found:
            print(f"[ERROR] Card not found: {card_id}")
            return jsonify({"status": "error", "message": "Card not found"}), 404

        # Create a context message for Claude
        context_message = f"User responded to {card_type or 'interactive card'} with action '{action}'"
        if form_data:
            context_message += f" and data: {form_data}"

        print(f"[DEBUG] Context message for Claude: {context_message}")

        # Add card interaction to message history for context
        messages.append(
            {
                "message_type": "card_interaction",
                "card_id": card_id,
                "action": action,
                "data": form_data,
                "hidden": True,  # This marks it as not displayed in UI
            }
        )

        # Get Claude's response to the card interaction
        claude_response = await get_claude_response(context_message)

        # Convert response to message objects
        new_messages = create_messages_from_response(claude_response)

        print(f"[DEBUG] New messages to return: {new_messages}")

        # Add all new messages to history
        messages.extend(new_messages)

        return jsonify(
            {
                "status": "success",
                "responses": new_messages,  # Return array of messages
            }
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/reset_session", methods=["POST"])
async def reset_session():
    """Reset the conversation session and clear message history."""
    global session_id, messages

    session_id = None
    messages.clear()

    return jsonify({"status": "success", "message": "Session reset successfully"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
