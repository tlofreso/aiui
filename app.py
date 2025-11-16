# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "quart",
#     "claude-agent-sdk>=0.1.6",
# ]
# ///

import os
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


def is_html_content(text: str) -> bool:
    """Check if the text appears to be HTML."""
    text = text.strip()
    # Simple heuristic: check if it starts with < or contains common HTML tags
    return text.startswith('<') or any(tag in text for tag in ['<div', '<html', '<body', '<p>', '<form'])


async def get_claude_response(user_message: str) -> str:
    """Get response from Claude SDK."""
    options = ClaudeAgentOptions(
        cwd=os.getcwd(),
        setting_sources=["user", "project"],
        allowed_tools=["Skill", "Read"]
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

        # Check if response is HTML and format accordingly
        if is_html_content(claude_response):
            response_message = {
                'chat_type': 'start',
                'message_type': 'card',
                'html': claude_response,
                'content': ''
            }
        else:
            response_message = {
                'chat_type': 'start',
                'content': claude_response
            }

        messages.append(response_message)

        return jsonify({
            'status': 'success',
            'response': response_message
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
