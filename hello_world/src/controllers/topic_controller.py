# src/controllers/topic_controller.py

from services import topic_service
from utils import response

def get_topics(event):
    subject = "Maths2"
    try:
        topics = topic_service.get_topics_by_subject_v2(subject)
        return response.success(topics)
    except Exception as error:
        return response.error(error)
