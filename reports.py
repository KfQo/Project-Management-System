import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def fetch_projects():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT name, budget, start_date, end_date, description FROM projects")
    data = c.fetchall()
    conn.close()
    return data

def generate_pdf_report(filename='Set name file .pdf '):
    projects = fetch_projects()
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Set Title ")

    y = height - 90
    c.setFont("Helvetica", 12)

    for i, project in enumerate(projects, start=1):
        name, budget, start_date, end_date, description = project
        lines = [
            f"Project {i}:",
            f"  Name       : {name}",
            f"  Budget     : ${budget}",
            f"  Start Date : {start_date}",
            f"  End Date   : {end_date}",
            f"  Description: {description}",
            ""
        ]
        for line in lines:
            c.drawString(50, y, line)
            y -= 20
            if y < 100:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 50

    c.save()
    print(f"PDF report saved as: {filename}")

# Run the report generation
generate_pdf_report()
