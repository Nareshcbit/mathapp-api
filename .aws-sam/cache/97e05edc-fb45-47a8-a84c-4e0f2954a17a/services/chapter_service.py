# src/services/chapter_service.py

from utils import dynamodb
import boto3

# Assuming that you have AWS credentials set up as environment variables or in AWS configuration
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MathApp')

def get_chapters_by_grade(subject, grade):
    primary_key_value = f"Chapter#{subject}#{grade}"
    # Query for grade chapters
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('PK').eq(primary_key_value)
    )

    # The response will contain items that match the query condition
    items = response['Items']
    return items
