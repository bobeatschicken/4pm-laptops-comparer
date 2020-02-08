import json
from pymongo import MongoClient

def return_workspaces(event, context):

    #Connect to MongoDB
    client = MongoClient("mongodb+srv://xxxx:xxxxxxx@cluster0-swsn8.mongodb.net/test?retryWrites=true&w=majority")
    db = client.compurator
    users_collection = db["users"]

    #remove later
    body = event

    authorizer_response = event

    #Event is the response returned by the authorizer
    user_google_id = authorizer_response["requestContext"]["authorizer"]["claims"]["sub"]
    print("USER ID", user_google_id)

    #Check to see if the user in the the user collections if not store into user collection
    cursor = users_collection.find({"google_client_id": user_google_id})
    print("CURSOR", cursor)

    print("doc", cursor[0])
    #print("TWO", cursor.next())



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
