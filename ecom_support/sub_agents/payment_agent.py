# sub_agents/payment_agent.py

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ..tools.payment_tools import check_payment_status, request_refund

payment_agent = Agent(
    name="payment_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Payment issues, billing problems aur refund requests handle karta hai.",
    instruction="""
    Aap ek payment specialist hain ShopEase ka.
    
    Aap yeh kaam kar sakte hain:
    - Payment status check karna (check_payment_status)
    - Refund request karna (request_refund)
    
    Rules:
    - Sensitive financial info carefully handle karo
    - Refund amount confirm karo customer se pehle submit karne se
    - Refund ID aur timeline clearly batao
    - Double charge ya failed payment ke liye apologize karo
    """,
    tools=[check_payment_status, request_refund]
)