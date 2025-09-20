import json
from src.app import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["message"] == "Hello!! We offer supports for all Digital Wallets and Payment Methods."
