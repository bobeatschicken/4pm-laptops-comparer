import json
from pymongo import MongoClient

def return_workspaces(event, context):

    #Connect to MongoDB
    client = MongoClient("mongodb+srv://XXX:XXXXX@cluster0-swsn8.mongodb.net/test?retryWrites=true&w=majority")
    db = client.compurator
    users_collection = db["users"]
    workspace_collection = db["workspaces"]

    #remove later
    body = event

    authorizer_response = event

    #Event is the response returned by the authorizer
    user_google_id = authorizer_response["requestContext"]["authorizer"]["claims"]["sub"]
    user_name = authorizer_response["requestContext"]["authorizer"]["claims"]["name"]
    
    print("USER ID", user_google_id)

    #Check to see if the user in the the user collections if not store into user collection
    cursor = users_collection.find({"google_client_id": user_google_id})
    if (cursor.count() == 0):
        new_user = { "google_client_id": user_google_id, "name": user_name }
        users_collection.insert_one(new_user)
    
    #Then find the workspaces for this user
    cursor = workspace_collection.find({"owner": user_google_id})
    #If there is no workspaces return no workspaces
    if (cursor.count() == 0):
        body = {"message":"This user does not have any workspaces set up."}
    else:
        body = list(cursor)
        print("body", body)

        for doc in cursor:
            print(doc)


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
