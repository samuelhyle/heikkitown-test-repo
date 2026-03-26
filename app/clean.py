"""Clean module for testing."""

def add(a, b):
    """Add two numbers."""
    return a + b

def format_date(date_str):
    """Format a date string safely."""
    from datetime import datetime
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return date_str
