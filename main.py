import os
import asyncio
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    AssistantMessage,
    TextBlock
)

async def main():
    options = ClaudeAgentOptions(
        cwd=os.getcwd(),
        setting_sources=["user", "project"],
        allowed_tools=["Skill", "Read"]
    )

    async with ClaudeSDKClient(options) as client:

        while True:
            user_input = input("You: ")
            await client.query(user_input)

            async for msg in client.receive_response():
                if isinstance(msg, AssistantMessage):
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            print(f"Claude: {block.text}")

asyncio.run(main())