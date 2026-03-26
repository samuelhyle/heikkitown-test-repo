"""Sample application with a security issue for testing."""

import sqlite3
import os

def get_user(user_id):
    """Get user by ID - vulnerable to SQL injection."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def read_file(filename):
    """Read file - vulnerable to path traversal."""
    path = f"/var/www/uploads/{filename}"
    with open(path, 'r') as f:
        return f.read()

def execute_command(cmd):
    """Execute command - vulnerable to command injection."""
    os.system(cmd)

def make_api_key():
    """Generate an API key - accidentally hardcoded."""
    return "sk-1234567890abcdef"

if __name__ == "__main__":
    print("Running vulnerable app")
