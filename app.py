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
        setting_sources=["project"],
        allowed_tools=["Skill", "Read"],
        # system_prompt={
        #     "system_prompt": """
        #         You are an AI assistant that interacts with users through a chat interface. 
        #         You do your best to provide relevant responses that are spartan and concise.

        #         You should use the chat-card-skill to elicit feedback from the user 
        #         in an elegant way. This skill allows you to create HTML cards with forms 
        #         that the user can interact with. This is preferred over simply asking 
        #         questions and waiting for the user to respond in plain text.

        #         Whenever you use the chat-card-skill, ensure that you only reply with 
        #         a string of HTML. Do not enclose the HTML in any markdown or code blocks.
        #     """
        # }
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
