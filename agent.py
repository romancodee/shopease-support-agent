from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Groq model define karo LiteLLM ke zariye
model = LiteLlm(
    model="groq/llama-3.3-70b-versatile"  # ya "groq/llama3-8b-8192" (faster)
)

# Agent banao
root_agent = Agent(
    name="my_groq_agent",
    model=model,
    description="you are help full assistant.",
    instruction="""
    you are help full assistant.
    give user answer to their questions clearly and concisly.
    """
)