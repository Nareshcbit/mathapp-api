import boto3
import json

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Use your desired region


def query_table(table_name, params):
    table = dynamodb.Table(table_name)
    try:
        response = table.query(**params)
        items = response.get('Items', [])
        print(f"Query succeeded: {json.dumps(items, indent=2)}")
        return items
    except Exception as e:
        print(f"Error querying table: {e}")
        raise e


def get_item(table_name, primary_key_value, sort_key_value):
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(
            Key={
                'PK': primary_key_value,
                'SK': sort_key_value
            }
        )
        item = response.get('Item')
        if item:
            print(f"Item fetched successfully: {json.dumps(item, indent=2)}")
            return item
        else:
            print("No item found with the given keys.")
            return None
    except Exception as e:
        print(f"Error getting item: {e}")
        raise e


if __name__ == '__main__':
    item = get_item('MathApp', 'QuestionBucket#Maths#Grade04', 'Decimals#Addition#0400')
    params = {
        'KeyConditionExpression': "#pk = :pkVal AND #sk = :skVal",
        'ExpressionAttributeNames': {
            "#pk": "PK",
            "#sk": "SK"
        },
        'ExpressionAttributeValues': {
            ":pkVal": 'QuestionBucket#Maths#Grade04',
            ":skVal": 'Decimals#Addition#0400'
        }
    }

    items = query_table('MathApp', params)
    print(items)
