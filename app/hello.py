"""Hello module."""

def say_hello(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

def format_date(date_str):
    """Format a date string."""
    from datetime import datetime
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return date_str
