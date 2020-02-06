import json
import boto3
import json

lambda_client = boto3.client('lambda')


def create_user(event, context):
    invoke_response = lambda_client.invoke(FunctionName="authorizer.handle",
                                           InvocationType='RequestResponse'
                                           )
    x = (invoke_response['Payload'].read())
    print(x)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "x" : x,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
