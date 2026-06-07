# tools/returns_tools.py

def check_return_eligibility(order_id: str) -> dict:
    """
    Check karta hai ke order return eligible hai ya nahi.
    Args:
        order_id: Order ID
    """
    eligible = {
        "ORD-9999": {"eligible": True, "reason": "30-day return window active hai."},
        "ORD-1234": {"eligible": True, "reason": "Item abhi delivered nahi hua."},
        "ORD-5678": {"eligible": False, "reason": "Return window expire ho gaya."},
    }
    result = eligible.get(order_id, {"eligible": False, "reason": "Order nahi mila."})
    return {"order_id": order_id, **result}


def initiate_return(order_id: str, reason: str) -> dict:
    """
    Return request start karta hai.
    Args:
        order_id: Order ID
        reason: Return ka reason (e.g. 'damaged', 'wrong item', 'not needed')
    """
    return {
        "success": True,
        "return_id": f"RET-{order_id[-4:]}",
        "message": f"Return request submit ho gayi. 3-5 din mein refund milega.",
        "reason": reason
    }