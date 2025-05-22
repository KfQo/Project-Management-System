# Project Management System

This project is a simple project management system built using Python and SQLite. It allows users to manage projects and their associated tasks, with functionalities to add projects, calculate costs, and generate PDF reports.

## Features

- Add projects with details such as name, budget, start date, end date, and description.
- Add tasks associated with each project, including task duration, cost, status, and assignee.
- Calculate the total estimated cost of projects.
- Generate PDF reports of project details.

## File Descriptions

- **models.py**: Defines the Project class.
- **app.py**: Main application for adding projects and tasks.
- **database.py**: Creates the necessary SQLite database tables.
- **reports.py**: Fetches project data and generates a PDF report.

## Requirements

- Python 3.x
- SQLite
- ReportLab library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KfQo/Project-Management-System
