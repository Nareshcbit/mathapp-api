# utils/response.py

import json

def success(data):
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }

def error(err):
    return {
        'statusCode': 500,
        'body': json.dumps({'message': str(err)})
    }
