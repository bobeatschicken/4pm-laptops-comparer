import os
import json
from pymongo import MongoClient
from bson import ObjectId

''' 
GET /workspaces endpoint
	Given a correct Google JWT token for a user, this endpoint will return all the workspaces of the user
	Also if the user has never logged into the account before, it will create on in the users collection

 '''
def get_workspaces(event, context):

	#Connect to MongoDB
	db_url = os.environ['DB_URL']
	print(f"Connecting to {db_url}")
	client = MongoClient(db_url)
	db = client.compurator
	users_collection = db["users"]
	workspace_collection = db["workspaces"]
	products_collection = db["products"]

	body = ""

	authorizer_response = event

	#Event is the response returned by the authorizer
	print("requestContext: ", authorizer_response["requestContext"]["authorizer"])
	user_google_id = authorizer_response["requestContext"]["authorizer"]["user_id"]
	user_name = authorizer_response["requestContext"]["authorizer"]["user_name"]

	#Check to see if the user in the the user collections if not store into user collection
	cursor = users_collection.find({"google_client_id": user_google_id})
	if (cursor.count() == 0):
		new_user = { "google_client_id": user_google_id, "name": user_name }
		users_collection.insert_one(new_user)

	#Then find the workspaces for this user
	cursor = workspace_collection.find({"owner": user_google_id})
	#If there is no workspaces return no workspaces
	if (cursor.count() == 0):
		body = {"workspaces":[]}
	else:
		#Return workspaces of the user
		build_body = {"workspaces": [] }

		for workspace in cursor:
			print("workspace", workspace)
			build_workspace = {"workspace_id": 0, "products": []}

			build_workspace["workspace_id"] = str(workspace["_id"])
			#Go through the products array and add product info
			products = workspace["products"]

			for p_id in products:
				#Get info from products collection
				product_cursor = products_collection.find({"p_id": p_id})

				if (product_cursor.count() == 0):
					#for some reason the product does not exist in product collection
					error = {"error": "This product does not exist."}
					build_workspace["products"].append(error)
				else:
					#a product is returned, there should not be more than one product per product id
					#Only for loop once but idk how to return just one
					for product in product_cursor:
						del product["_id"] #Deleted the _id that is auto generated from Mongo
						build_workspace["products"].append(product)
			build_body["workspaces"].append(build_workspace)
		body = build_body

		print(body)

	response = {
		"statusCode": 200,
		"body": json.dumps(body)
	}

	return response


''' 
GET /workspaces/{workspaceId} endpoint
	Given a correct Google JWT token for a user, this endpoint will return the workspaces of the specified ID
	Should only work if the user owns that workspace

 '''
def get_workspace_by_id(event, context):
	#Connect to MongoDB
	db_url = os.environ['DB_URL']
	print(f"Connecting to {db_url}")
	client = MongoClient(db_url)
	db = client.compurator
	users_collection = db["users"]
	workspace_collection = db["workspaces"]
	products_collection = db["products"]

	body = ""

	authorizer_response = event


	#Event is the response returned by the authorizer
	print("requestContext: ", authorizer_response["requestContext"]["authorizer"])
	user_google_id = authorizer_response["requestContext"]["authorizer"]["user_id"]
	user_name = authorizer_response["requestContext"]["authorizer"]["user_name"]
	workspaceId = authorizer_response["pathParameters"]["workspaceId"]

	print("workpace id", workspaceId)
	#Then find the workspaces for this user
	cursor = workspace_collection.find({"_id": ObjectId(workspaceId)})

	#If there is no workspaces return no workspaces
	if (cursor.count() == 0):
		body = {"products":[]}
	else:
		#Return workspaces of the user
		build_body = {"products": [] }
		for workspace in cursor:
			print("workspace", workspace)
			products = workspace["products"]

			for p_id in products:
				#Get info from products collection
				product_cursor = products_collection.find({"p_id": p_id})

				if (product_cursor.count() == 0):
					#for some reason the product does not exist in product collection
					error = {"error": "This product does not exist."}
					build_body["products"].append(error)
				else:
					#a product is returned, there should not be more than one product per product id
					#Only for loop once but idk how to return just one
					for product in product_cursor:
						del product["_id"] #Deleted the _id that is auto generated from Mongo
						build_body["products"].append(product)
			body = build_body


	response = {
		"statusCode": 200,
		"body": json.dumps(body)
	}

	return response
