def get_order_status(order_id :str) -> str:
    """
    return the order current status
    Args:
        order_id : Order ID (e.g., "ORD12345")
    """
    # fake data base
    orders = {
        "ORD-1234": {"status": "Shipped", "item": "Nike Shoes", "date": "2024-06-01"},
        "ORD-5678": {"status": "Processing", "item": "Samsung TV", "date": "2024-06-05"},
        "ORD-9999": {"status": "Delivered", "item": "iPhone Case", "date": "2024-05-28"},
    }
    
    if order_id in orders:
        return {"success": True, "order_id": order_id, "status": orders[order_id]["status"]}
    
    return {"success": False, "message": "Order ID not found."}
    
def get_order_history(customer_id :str) -> list:
    """
    return the order history for a given customer
    Args:
        customer_id : Customer ID (e.g., "CUST12345")
    """
    # fake data base
    customers = {
        "CUST-001": [
            {"order_id": "ORD-1234", "item": "Nike Shoes", "date": "2024-06-01"},
            {"order_id": "ORD-5678", "item": "Samsung TV", "date": "2024-06-05"},
        ],
        "CUST-002": [
            {"order_id": "ORD-9999", "item": "iPhone Case", "date": "2024-05-28"},
        ],
    }
    
    if customer_id in customers:
        return {"success": True, "customer_id": customer_id, "orders": customers[customer_id]}
    
    return {"success": False, "message": "Customer ID not found."}