"""New feature with vulnerability."""

import sqlite3
import os

def get_data(user_id):
    """Get user data - SQL Injection."""
    db = sqlite3.connect('data.db')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query).fetchall()

def run_shell(cmd):
    """Execute command - injection risk."""
    os.system(cmd)
