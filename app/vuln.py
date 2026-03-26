"""Vulnerable module for testing."""

import sqlite3
import os

def get_user(user_id):
    """Get user - SQL Injection vulnerability."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def execute_cmd(cmd):
    """Command injection vulnerability."""
    os.system(cmd)

def api_key():
    """Hardcoded secret."""
    return "sk-abcdef123456789"
