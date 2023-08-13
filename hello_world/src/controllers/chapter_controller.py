# src/controllers/chapter_controller.py

from services import chapter_service
from utils import response

def get_chapters(event):
    params = event.get('queryStringParameters', {})
    subject = params.get('subject')
    grade = params.get('grade')

    try:
        chapters = chapter_service.get_chapters_by_grade(subject, grade)
        return response.success(chapters)
    except Exception as error:
        return response.error(error)
