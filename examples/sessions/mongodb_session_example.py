import asyncio
import os
import warnings
from dotenv import load_dotenv

from google.adk.runners import Runner
from google.genai import types

from adk_extra_services.sessions import MongoSessionService
from uppercase_agent import uppercase_agent


APP_NAME = "mongodb_session_example"
USER_ID = "example_user"
SESSION_ID = "session1"


def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if not os.path.exists(dotenv_path):
        warnings.warn(
            f'Missing .env file at {dotenv_path}. See .env.example for an example.'
        )
    else:
        load_dotenv(dotenv_path, override=True, verbose=True)

        
async def main():
    session_service = MongoSessionService(
        mongo_url="mongodb://localhost:27017",
        db_name="adk_sessions",
    )

    runner = Runner(
        agent=uppercase_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    user_prompt = "Convert the following text to uppercase: 'Real Madrid is better than Barcelona.'"
    print(f">>> Sending to agent: {user_prompt}")
    user_content = types.Content(role="user", parts=[types.Part(text=user_prompt)])
    final_response = None
    async for event in runner.run_async(
        user_id=USER_ID, session_id=SESSION_ID, new_message=user_content
    ):
        if event.is_final_response() and event.content:
            final_response = event.content.parts[0].text
    print("Agent response:", final_response)

if __name__ == "__main__":
    load_env()
    asyncio.run(main())