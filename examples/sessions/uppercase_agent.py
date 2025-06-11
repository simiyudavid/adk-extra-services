from google.adk.agents import Agent


async def uppercase_text(text: str) -> str:
    """Convert the input text to uppercase."""
    return text.upper()

uppercase_agent = Agent(
    name="uppercase_agent",
    model="gemini-2.0-flash",
    description="Agent that converts text to uppercase.",
    instruction="Use the uppercase_text tool to transform the input text to uppercase.",
    tools=[uppercase_text],
)
