from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ..tools.order_tools import get_order_status, get_order_history

order_agent = Agent(
    name="order_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="manage the order status and order history and handle order detail.",
    instruction="""you are specilized order management agent
    
    you are authorized 
    - check the order status by order id using get_order_status tool
    - check the order history by customer id using get_order_history tool
    
    Rules:
    - Always use the tools when you need to check order status or order history.
    - If the user asks for order status, use get_order_status tool with the provided order id.
    - If the user asks for order history, use get_order_history tool with the provided customer
    id.
    -  dont give the thing which is not related to order status and order history. with out give order id and customer id.
    """,
    tools=[get_order_status, get_order_history]
)