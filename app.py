# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "quart",
#     "claude-agent-sdk>=0.1.6",
# ]
# ///

import os
import uuid
from quart import Quart, render_template, request, jsonify
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    AssistantMessage,
    TextBlock
)

app = Quart(__name__)

# In-memory message storage
messages = []


async def get_claude_response(user_message: str) -> str:
    """Get response from Claude SDK."""

    options = ClaudeAgentOptions(
        cwd=os.getcwd(),
        setting_sources=["project"],
        allowed_tools=["Skill", "Read"],
        system_prompt="""
            Use your chat-card-skill to help the user with requests.

            When you want to send both a text message and a card:
            - Simply output the text first, followed by the HTML card
            - No special formatting needed, just natural flow

            When sending just a card:
            - Output only the HTML, nothing else

            For HTML cards, do not enclose in markdown code blocks - just provide the raw HTML.
        """
    )

    response_text = ""

    async with ClaudeSDKClient(options) as client:
        await client.query(user_message)

        async for msg in client.receive_response():
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock):
                        response_text += block.text

    return response_text


def split_text_and_html(response: str) -> tuple[str, str]:
    """
    Split a response into text and HTML parts.
    Returns (text_part, html_part) where either or both may be empty strings.
    """
    response = response.strip()

    if not response:
        return "", ""

    # Common HTML opening tags to look for
    html_tags = ['<div', '<html', '<body', '<form', '<section', '<article', '<main']

    # Find the first occurrence of any HTML tag
    html_start = -1
    for tag in html_tags:
        pos = response.find(tag)
        if pos != -1 and (html_start == -1 or pos < html_start):
            html_start = pos

    # No HTML found
    if html_start == -1:
        return response, ""

    # HTML found at the beginning
    if html_start == 0:
        return "", response

    # HTML found after some text
    text_part = response[:html_start].strip()
    html_part = response[html_start:].strip()

    return text_part, html_part


def create_messages_from_response(response: str) -> list:
    """
    Convert Claude's response into message objects.
    Splits text and HTML content into separate messages.
    Returns a list of message dicts to be added to the messages array.
    """
    new_messages = []

    # Split the response
    text_part, html_part = split_text_and_html(response)

    # Add text message if present
    if text_part:
        new_messages.append({
            'chat_type': 'start',
            'content': text_part
        })

    # Add card if present
    if html_part:
        card_id = str(uuid.uuid4())
        new_messages.append({
            'chat_type': 'start',
            'message_type': 'card',
            'card_id': card_id,
            'html': html_part,
            'content': '',
            'card_submitted': False
        })

    return new_messages


@app.route('/')
async def index():
    """Render the chat interface."""
    return await render_template(
        'chat.html',
        page_title='AI Chat',
        messages=messages
    )


@app.route('/api/send_message', methods=['POST'])
async def send_message():
    """Handle incoming chat messages."""
    try:
        data = await request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({
                'status': 'error',
                'message': 'Message cannot be empty'
            }), 400

        # Add user message to history
        messages.append({
            'chat_type': 'end',
            'content': user_message
        })

        # Get Claude response
        claude_response = await get_claude_response(user_message)

        # Convert response to message objects
        new_messages = create_messages_from_response(claude_response)

        # Add all new messages to history
        messages.extend(new_messages)

        return jsonify({
            'status': 'success',
            'responses': new_messages  # Return array of messages
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/card_action', methods=['POST'])
async def card_action():
    """Handle card interaction submissions."""
    try:
        data = await request.get_json()
        card_id = data.get('card_id')
        action = data.get('action')
        form_data = data.get('data', {})

        if not card_id or not action:
            return jsonify({
                'status': 'error',
                'message': 'card_id and action are required'
            }), 400

        # Find the card in messages and mark as submitted
        card_found = False
        card_type = None
        for msg in messages:
            if msg.get('card_id') == card_id:
                msg['card_submitted'] = True
                # Try to extract card_type from HTML if present
                html = msg.get('html', '')
                if 'data-card-type=' in html:
                    start = html.find('data-card-type="') + len('data-card-type="')
                    end = html.find('"', start)
                    card_type = html[start:end] if end > start else 'unknown'
                card_found = True
                break

        if not card_found:
            return jsonify({
                'status': 'error',
                'message': 'Card not found'
            }), 404

        # Create a context message for Claude
        context_message = f"User responded to {card_type or 'interactive card'} with action '{action}'"
        if form_data:
            context_message += f" and data: {form_data}"

        # Add card interaction to message history for context
        messages.append({
            'message_type': 'card_interaction',
            'card_id': card_id,
            'action': action,
            'data': form_data,
            'hidden': True  # This marks it as not displayed in UI
        })

        # Get Claude's response to the card interaction
        claude_response = await get_claude_response(context_message)

        # Convert response to message objects
        new_messages = create_messages_from_response(claude_response)

        # Add all new messages to history
        messages.extend(new_messages)

        return jsonify({
            'status': 'success',
            'responses': new_messages  # Return array of messages
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
