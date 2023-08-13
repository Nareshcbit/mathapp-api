import boto3
import random
import json

# Assuming that you have AWS credentials set up as environment variables or in AWS configuration
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MathApp')

def get_questions(subject, topic, sub_topic=None, min_level=None, max_level=None):
    print("getQuestions")
    print(subject, topic, sub_topic, min_level, max_level)
    
    primary_key_value = f"Topic#{subject}#{topic}"
    params = {}
    
    if sub_topic and min_level and max_level:
        start_key_val = f"Question#{sub_topic}#{min_level}#000"
        end_key_val = f"Question#{sub_topic}#{max_level}#999"
        
        params = {
            'KeyConditionExpression': '#pk = :pkVal AND #sk BETWEEN :startKey AND :endKey',
            'ExpressionAttributeNames': {
                '#pk': 'PK',
                '#sk': 'SK'
            },
            'ExpressionAttributeValues': {
                ':pkVal': primary_key_value,
                ':startKey': start_key_val,
                ':endKey': end_key_val
            }
        }
    
    print(json.dumps(params))
    response = table.query(**params)
    items = response.get('Items', [])

    if len(items) > 10:
        random_items = random.sample(items, 10)
        return random_items

    return items

def get_questions_v1(subject, topic, sub_topic="defaultSubTopic", category="defaultCategory"):
    primary_key_value = f"Topic#{subject}-{topic}"
    sort_key_value = None
    sort_key_condition = None

    if sub_topic == "defaultSubTopic" and category == "defaultCategory":
        sort_key_value = "Question#"
        sort_key_condition = 'begins_with(#sk, :skVal)'
    else:
        sort_key_value = f"Question#{sub_topic}-{category}-"
        sort_key_condition = 'begins_with(#sk, :skVal)'

    response = table.query(
        KeyConditionExpression="#pk = :pkVal AND " + sort_key_condition,
        ExpressionAttributeNames={
            '#pk': 'PK',
            '#sk': 'SK'
        },
        ExpressionAttributeValues={
            ':pkVal': primary_key_value,
            ':skVal': sort_key_value
        }
    )

    items = response.get('Items', [])

    return items
