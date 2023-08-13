# src/controllers/question_controller.py

from services import question_service
from utils import response

def get_questions(event):
    params = event.get('queryStringParameters', {})
    subject = params.get('subject')
    topic = params.get('topic')
    sub_topic = params.get('subTopic')
    min_level = params.get('minLevel')
    max_level = params.get('maxLevel')

    try:
        questions = question_service.get_questions(subject, topic, sub_topic, min_level, max_level)
        return response.success(questions)
    except Exception as error:
        return response.error(error)
