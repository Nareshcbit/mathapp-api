# src/routes/topic_routes.py

from controllers import topic_controller

def get(event):
    return topic_controller.get_topics(event)
