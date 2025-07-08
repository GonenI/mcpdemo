from fastmcp import FastMCP
import random
import sqlite3
import os

mcp = FastMCP()

# Task list and counter for cycling through tasks
_task_list = [
    "Write a quicksort algorithm for a list",
    "create a function to swap two numbers", 
    "write a function to return a random permutation of the given string",
    "write a function to return the ascii checksum of a string"
]
_task_counter = 0

@mcp.tool()
def getfunctionname() -> str:
    """Return a random function name according to some logic"""
    prefixes = ["Function", "Util", "Helper", "Impl"]
    prefix = random.choice(prefixes)
    number = str(random.randint(0, 9999)).zfill(4)
    result = f"{prefix}{number}"
    return result

@mcp.tool()
def getNextTask() -> str:
    """Return the next task in the list for AI implementation"""
    global _task_counter
    task = _task_list[_task_counter]
    _task_counter = (_task_counter + 1) % len(_task_list)
    return task

@mcp.tool()
def getnextbugtofix() -> str:
    """Return the next bug to fix from the SQLite database"""
    db_path = "bugs.db"
    
    # Check if database exists
    if not os.path.exists(db_path):
        return "Database not found. Please run setup_bugs_db.py first to create the bugs database."
    
    try:
        # Read from database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get a random bug
        cursor.execute('SELECT id, date, description FROM bugs ORDER BY RANDOM() LIMIT 1')
        result = cursor.fetchone()
        conn.close()
        
        if result:
            bug_id, date, description = result
            return f"Bug #{bug_id} ({date}): {description}"
        else:
            return "No bugs found in database"
    except sqlite3.Error as e:
        return f"Database error: {e}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)


