#!/usr/bin/env python3
"""
Setup script for the bugs database.
Run this script once to create the bugs.db file with sample data.
"""

import sqlite3
import os

def create_bugs_database():
    """Create the bugs database with sample data"""
    db_path = "bugs.db"
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing {db_path}")
    
    # Create new database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create bugs table
    cursor.execute('''
        CREATE TABLE bugs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    
    # Insert sample data
    sample_bugs = [
        ("2025-07-01", "Login form validation not working properly"),
        ("2025-07-02", "Memory leak in data processing module"),
        ("2025-07-03", "API returns 500 error for large payloads"),
        ("2025-07-04", "UI elements misaligned on mobile devices"),
        ("2025-07-05", "Database connection timeout in production"),
        ("2025-07-06", "Search functionality returns incorrect results"),
        ("2025-07-07", "File upload fails for files larger than 10MB"),
        ("2025-07-08", "Password reset email not being sent"),
        ("2025-07-09", "Session management causes duplicate logins"),
        ("2025-07-10", "Export feature crashes with special characters")
    ]
    
    cursor.executemany('INSERT INTO bugs (date, description) VALUES (?, ?)', sample_bugs)
    conn.commit()
    
    # Verify the data was inserted
    cursor.execute('SELECT COUNT(*) FROM bugs')
    count = cursor.fetchone()[0]
    print(f"Created bugs.db with {count} bug records")
    
    conn.close()

if __name__ == "__main__":
    create_bugs_database()
