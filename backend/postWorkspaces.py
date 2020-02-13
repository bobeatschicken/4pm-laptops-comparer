import json
from pymongo import MongoClient
import sys

from mongoSetup import connect_database, get_user_auth, check_user

# connects to MongoDB
db = connect_database()

# POST /workspaces
# Creates a new workspace, returns the id of the workspace
def create_workspace(event, context):
	global db

	body = {}

	authorizer_response = event

	try:
		user_info = get_user_auth(event)

		# Create new workspace owned by user with default untitled name
		new_workspace = {"owner": user_info["g_id"], "name": "Untitled Workspace", "products": []}
		new_id = db.workspaces.insert_one(new_workspace).inserted_id
		print("new workspace inserted, workspace id:", str(new_id))
		body["_id"] = str(new_id)

		response = {
			"statusCode": 200,
			"body": json.dumps(body)
		}
		return response
	except:
		e = sys.exc_info()[0]
		errorCode = {"code": 1}
		errorCode["message"] = "ERROR: " + str(e)
		response = {
			"statusCode": 200,
			"errorCode": json.dumps(errorCode),
			"body": json.dumps(body)
		}
		print("ERROR:", sys.exc_info()[1])
		return response


