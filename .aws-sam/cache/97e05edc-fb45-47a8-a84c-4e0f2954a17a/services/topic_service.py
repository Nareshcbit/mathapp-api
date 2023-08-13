# src/services/topic_service.py

from utils import dynamodb

TABLE_NAME = "MathApp"

def get_topics_by_subject_v2(subject):
    primary_key_value = f"Subject#{subject}"
    item = dynamodb.get_item(TABLE_NAME, primary_key_value, '#SUBJECTMETA')
    if 'PK' in item:
        del item['PK']
    if 'SK' in item:
        del item['SK']
    return item
