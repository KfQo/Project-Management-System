# app.py
import sqlite3
from datetime import datetime

# Function to calculate the total expected cost
def calculate_total_cost(tasks):
    total_cost = sum(task['cost'] for task in tasks)
    return total_cost

# Function to add project and tasks
def add_project():
    # Get project details from the user
    name = input("Enter the project name: ")
    budget = float(input("Enter the project budget: "))
    start_date = input("Enter the project start date (YYYY-MM-DD): ")
    end_date = input("Enter the project end date (YYYY-MM-DD): ")
    description = input("Enter a description for the project: ")

    # Add the project to the database
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO projects (name, budget, start_date, end_date, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, budget, start_date, end_date, description))
    project_id = c.lastrowid  # Get the last inserted project ID

    # Get task details
    tasks = []
    while True:
        task_name = input("\nEnter the task name (or type 'done' to finish): ")
        if task_name.lower() == 'done':
            break
        
        task_duration = int(input(f"Enter the duration for task '{task_name}' in days: "))
        task_cost = float(input(f"Enter the estimated cost for task '{task_name}': "))
        task_status = input(f"Enter the status for task '{task_name}': ")
        task_assignee = input(f"Enter the assignee for task '{task_name}': ")
        task_start_date = input(f"Enter the start date for task '{task_name}' (YYYY-MM-DD): ")
        task_end_date = input(f"Enter the end date for task '{task_name}' (YYYY-MM-DD): ")

        # Store the task
        tasks.append({
            'name': task_name,
            'duration': task_duration,
            'cost': task_cost,
            'status': task_status,
            'assignee': task_assignee,
            'start_date': task_start_date,
            'end_date': task_end_date
        })

    # Add tasks to the database
    for task in tasks:
        c.execute('''
            INSERT INTO tasks (project_id, name, duration, cost, status, assignee, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (project_id, task['name'], task['duration'], task['cost'], task['status'], task['assignee'], task['start_date'], task['end_date']))

    total_cost = calculate_total_cost(tasks)
    print(f"\n✅ Project '{name}' added successfully!")
    print(f"Total estimated cost for the project: {total_cost}")

    conn.commit()
    conn.close()

# Main function
if __name__ == "__main__":
    print("Welcome to the Smart Project Manager!")
    add_project()
