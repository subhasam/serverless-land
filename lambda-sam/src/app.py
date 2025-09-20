import json

def lambda_handler(event, context):
    """
    Lambda function to return a simple 'Hello, World!' message.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello!! We offer supports for all Digital Wallets and Payment Methods.",
            "input": event
        })
    }