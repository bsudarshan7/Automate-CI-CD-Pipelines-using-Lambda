import json
from datetime import datetime

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "application": "Lambda CI/CD Demo",
            "version": "1.0",
            "deployed_at": str(datetime.utcnow()),
            "status": "Running Successfully"
        })
    }
