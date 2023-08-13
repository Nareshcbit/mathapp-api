# app.py
import json

from routes import topic_routes, question_routes

def lambda_handler(event, context):
    print(json.dumps(event))
    return route(event)

def route(event):
    path = event.get('path', '')

    if path == '/math/topics':
        return topic_routes.get(event)
    elif path == '/math/questions':
        return question_routes.get(event)
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Not Found'})
        }
