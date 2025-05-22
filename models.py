# models.py
class Project:
    def __init__(self, name, budget, deadline, description):
        self.name = name
        self.budget = budget
        self.deadline = deadline
        self.description = description
