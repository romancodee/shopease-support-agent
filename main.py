import asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.genai.types import Content as genai_content, Part
from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService


# import agent from agent.py
from agent import root_agent

# in memory session service store everything in memory, you can also use other session services like RedisSessionService
session_service = InMemorySessionService()

#runner bind the session service and the agent together and provides an interface to interact with the agent
# app name is used to identify the app in the session service, you can use any name you want and all
# sessions created by this runner will be stored under this app name in the session service
runner = Runner(
    agent=root_agent,
    session_service=session_service,
    app_name="my_groq_agent_app"
)

async def main():
    # user id is used to identify the user in the session service, you can use any id you want and all
    #app name in session service will be a combination of app name and user id, so that sessions are stored separately for each user
    # session id to identify the session in the session service, you can use any id you want and it will be used to store the conversation history and other session data in the session service
    
    user_id = "user_123"
    session_id = "session_123"
    app_name = "my_groq_agent_app"
    
    # create a session for the user
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    
    
    # user message to the agent
    
    user_message = genai_content(parts=[Part(text="what is the capital of france?")])
    
    
        # --- 6. The Event Loop ---
    # runner.run_async() returns an async generator of Event objects.
    # It does NOT return a string. You must iterate to get anything.
    print("Agent: ", end="", flush=True)

# the event loop
    async for event in runner.run_async(
        new_message=user_message,
        user_id=user_id,
        session_id=session_id
    ):
        
        if event.is_final_response():
            if event.content and event.content.parts:
                 for part in event.content.parts:
                     if part.text:
                            print(part.text);
                            
asyncio.run(main())                            