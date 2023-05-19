import json

def hello(event, context):
	return {"statusCode": 200, "body": event.get('queryStringParameters') }
