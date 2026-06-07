# tools/payment_tools.py

def check_payment_status(order_id: str) -> dict:
    """
    Payment status check karta hai.
    Args:
        order_id: Order ID
    """
    payments = {
        "ORD-1234": {"status": "Paid", "method": "Credit Card", "amount": 5999},
        "ORD-5678": {"status": "Pending", "method": "Bank Transfer", "amount": 45000},
        "ORD-9999": {"status": "Refunded", "method": "JazzCash", "amount": 799},
    }
    if order_id in payments:
        return {"success": True, "payment": payments[order_id]}
    return {"success": False, "message": "Payment info nahi mili."}


def request_refund(order_id: str, amount: float) -> dict:
    """
    Refund request karta hai.
    Args:
        order_id: Order ID
        amount: Refund amount (PKR mein)
    """
    return {
        "success": True,
        "refund_id": f"REF-{order_id[-4:]}",
        "amount": amount,
        "message": f"Rs. {amount} ka refund 5-7 business days mein original account mein aayega."
    }