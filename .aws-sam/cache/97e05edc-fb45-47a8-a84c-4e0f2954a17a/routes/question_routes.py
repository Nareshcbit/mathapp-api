# src/routes/question_routes.py

from controllers import question_controller

def get(event):
    return question_controller.get_questions(event)
