# tools/delivery_tools.py

def track_delivery(order_id: str) -> dict:
    """
    Delivery tracking information return karta hai.
    Args:
        order_id: Order ID
    """
    tracking = {
        "ORD-1234": {
            "carrier": "TCS",
            "tracking_number": "TCS-789456",
            "current_location": "Lahore Hub",
            "expected_delivery": "2024-06-08",
            "status": "In Transit"
        },
        "ORD-5678": {
            "carrier": "Leopards",
            "tracking_number": "LEO-123789",
            "current_location": "Warehouse",
            "expected_delivery": "2024-06-10",
            "status": "Processing"
        },
    }
    if order_id in tracking:
        return {"success": True, "tracking": tracking[order_id]}
    return {"success": False, "message": "Tracking info nahi mili."}


def report_delivery_issue(order_id: str, issue_type: str) -> dict:
    """
    Delivery issue report karta hai.
    Args:
        order_id: Order ID
        issue_type: Issue type ('not_received', 'damaged', 'wrong_address', 'delayed')
    """
    return {
        "success": True,
        "ticket_id": f"TKT-{order_id[-4:]}-DEL",
        "message": f"Delivery issue report ho gaya. Team 24 ghante mein contact karegi.",
        "issue": issue_type
    }