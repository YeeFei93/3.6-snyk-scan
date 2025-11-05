import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    """
    AWS Lambda function that returns a Hello World message with AWS metadata
    """
    print("Hello, World!")
    
    # Get some AWS context information (common in real Lambda functions)
    try:
        # This would work in actual AWS Lambda environment
        region = context.invoked_function_arn.split(':')[3] if context else 'local'
    except:
        region = 'local'
    
    response_body = {
        'message': 'Hello, World!',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'region': region,
        'function_name': context.function_name if context else 'hello-world-lambda'
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response_body)
    }