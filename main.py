import asyncio
import os

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
)

CHAT_RESPONSE_SCHEMA = {
    "type": "json_schema",
    "schema": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": "Optional text message intended for the human user. Can be empty string if only sending HTML.",
            },
            "html": {
                "type": "string",
                "description": "Optional HTML content containing a DaisyUI chat card. Must be valid, complete HTML following the chat-card-skill patterns. Can be empty string if only sending a message.",
            },
        },
        "required": ["message", "html"],
        "additionalProperties": False,
    },
}


async def main():
    options = ClaudeAgentOptions(
        cwd=os.getcwd(),
        setting_sources=["user", "project"],
        allowed_tools=["Skill", "Read"],
        output_format=CHAT_RESPONSE_SCHEMA,
    )

    async with ClaudeSDKClient(options) as client:
        while True:
            user_input = input("You: ")
            await client.query(user_input)

            async for msg in client.receive_response():
                if isinstance(msg, ResultMessage):
                    # Check for structured output in ResultMessage
                    if hasattr(msg, 'structured_output') and msg.structured_output:
                        output = msg.structured_output
                        if output.get('message'):
                            print(f"Claude: {output['message']}")
                        if output.get('html'):
                            print(f"HTML: {output['html']}")
                elif isinstance(msg, AssistantMessage):
                    # Regular text blocks from assistant
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            print(f"Claude: {block.text}")


asyncio.run(main())
