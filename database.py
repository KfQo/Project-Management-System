# database.py
import sqlite3

def create_tables():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    
    # Create the 'projects' table with the necessary columns
    c.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            budget REAL,
            start_date TEXT,
            end_date TEXT,
            description TEXT
        )
    ''')

    # Create the 'tasks' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            name TEXT,
            duration INTEGER,  -- Task duration in days
            cost REAL,         -- Estimated cost of the task
            status TEXT,       -- Task status
            assignee TEXT,     -- Assigned team member
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
