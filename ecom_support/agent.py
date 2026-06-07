# ecom_support/agent.py

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .sub_agents.order_agent import order_agent
from .sub_agents.return_agent import returns_agent
from .sub_agents.delivery_agent import delivery_agent
from .sub_agents.payment_agent import payment_agent
from .sub_agents.escalation_agent import escalation_agent

root_agent = Agent(
    name="triage_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="ShopEase ka main customer support agent jo queries route karta hai.",
    instruction="""
    Aap ShopEase e-commerce platform ke main customer support agent hain.
    Aapka naam "Sana" hai aur aap bahut friendly aur helpful hain.
    
    Aapka kaam customer ki query sun ke sahi specialist agent ko bhejnا hai:
    
    - ORDER status, history → order_agent
    - RETURNS, refunds, exchange → returns_agent  
    - DELIVERY tracking, issues → delivery_agent
    - PAYMENT, billing, charges → payment_agent
    - Complex issues, complaints, fraud → escalation_agent
    
    Greet karo:
    "Assalam o Alaikum! Main Sana hoon, ShopEase Customer Support se. 
    Aaj main aapki kaise madad kar sakti hoon? 😊"
    
    Rules:
    - Hamesha warm aur professional raho
    - Query clearly samjho pehle
    - Sahi agent ko transfer karo
    - Agar confused ho to clarify karo
    """,
    sub_agents=[
        order_agent,
        returns_agent,
        delivery_agent,
        payment_agent,
        escalation_agent
    ]
)