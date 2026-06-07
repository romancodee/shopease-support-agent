from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

# Groq model define karo LiteLLM ke zariye
model = LiteLlm(
    model="groq/llama-3.3-70b-versatile"  # ya "groq/llama3-8b-8192" (faster)
)

# Agent banao
root_agent = Agent(
    name="my_groq_agent",
    model=model,
    description="Ek helpful agent jo Groq ke saath chalata hai.",
    instruction="""
    Aap ek helpful assistant hain.
    User ke sawalon ka jawab clearly aur concisely dein.
    """
)