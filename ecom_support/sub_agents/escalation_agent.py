# sub_agents/escalation_agent.py

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def create_escalation_ticket(
    customer_name: str,
    issue_description: str,
    priority: str
) -> dict:
    """
    Human agent ke liye escalation ticket banata hai.
    Args:
        customer_name: Customer ka naam
        issue_description: Issue ki detail
        priority: 'low', 'medium', 'high', 'urgent'
    """
    import random
    ticket_id = f"ESC-{random.randint(10000, 99999)}"
    wait_times = {"low": "48 ghante", "medium": "24 ghante",
                  "high": "4 ghante", "urgent": "1 ghanta"}
    return {
        "success": True,
        "ticket_id": ticket_id,
        "priority": priority,
        "wait_time": wait_times.get(priority, "24 ghante"),
        "message": f"Aapka case {ticket_id} number se human agent ko transfer ho gaya."
    }

escalation_agent = Agent(
    name="escalation_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Complex issues aur complaints ko human agents tak escalate karta hai.",
    instruction="""
    Aap ek escalation specialist hain ShopEase ka.
    
    Aap tab kaam karte hain jab:
    - Issue bahut complex ho
    - Customer bahut naraaz ho
    - Doosre agents solve na kar sakein
    - Legal ya fraud matter ho
    
    Priority levels:
    - urgent: Fraud, security breach
    - high: Bahut naraaz customer, bada amount
    - medium: Normal unresolved issues
    - low: Feedback, suggestions
    
    Rules:
    - Customer ko ticket ID zaroor do
    - Expected wait time batao
    - Apologize karo inconvenience ke liye
    - Assure karo ke problem solve hogi
    """,
    tools=[create_escalation_ticket]
)