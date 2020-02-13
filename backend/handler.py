import os
import json
from scrape_amazon.update_product_db_amazon import check_product_exists, add_product_amazon
from pymongo import MongoClient
from bson import ObjectId


def get_workspaces(event, context):
	''' 
	GET /workspaces endpoint
	Given a correct Google JWT token for a user, this endpoint will return all the workspaces of the user
	Also if the user has never logged into the account before, it will create on in the users collection

	'''

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
			build_workspace = {"workspace_id": 0, "workspace_name": "", "products": []}
			build_workspace["name"] = workspace["name"]
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
		"body": json.dumps(body),
		"headers": {
			"Access-Control-Allow-Origin": "*"
		}
	}

	return response



def get_workspace_by_id(event, context):
	''' 
	GET /workspaces/{workspaceId} endpoint
	Given a correct Google JWT token for a user, this endpoint will return the workspaces of the specified ID
	Should only work if the user owns that workspace

 	'''
	#Connect to MongoDB
	db_url = os.environ['DB_URL']
	print(f"Connecting to {db_url}")
	client = MongoClient(db_url)
	db = client.compurator
	users_collection = db["users"]
	workspace_collection = db["workspaces"]
	products_collection = db["products"]

	body = ""
	statusCode = 200

	authorizer_response = event


	#Event is the response returned by the authorizer
	print("requestContext: ", authorizer_response["requestContext"]["authorizer"])
	user_google_id = authorizer_response["requestContext"]["authorizer"]["user_id"]
	user_name = authorizer_response["requestContext"]["authorizer"]["user_name"]
	workspaceId = authorizer_response["pathParameters"]["workspaceId"]

	print("workpace id", workspaceId)
	#Then find the workspaces for this user
	cursor = workspace_collection.find({"_id": ObjectId(workspaceId)})

	#If workspace does not exist return 404
	if (cursor.count() == 0):
		statusCode = 404
		body = {"Error":"Workspace does not exist!"}
	else:
		#Return workspaces of the user
		build_body = {"name":"","products": [] }
		for workspace in cursor:
			build_body["name"] = workspace["name"]
			#if the user does not own the workspace
			if (workspace["owner"] != user_google_id):
				build_body = {"error": "User does not own this workspace."}

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
		"statusCode": statusCode,
		"body": json.dumps(body),
		"headers": {
			"Access-Control-Allow-Origin": "*"
		}
	}

	return response



def patch_workspace_by_id(event, context):
	''' 
	PATCH /workspaces/{workspaceId} endpoint
	Given a correct Google JWT token and correct json for an updated workspace
	endpoint will update the workspace with new info
	Format for PATCH JSON
	
	Each field is optional, the ones that are specified will be updated into the workspace.
	{
		"name" : "new title" 
		"products" : [new_products_array] 
	}

	'''

	#Connect to MongoDB
	db_url = os.environ['DB_URL']
	print(f"Connecting to {db_url}")
	client = MongoClient(db_url)
	db = client.compurator
	users_collection = db["users"]
	workspace_collection = db["workspaces"]
	products_collection = db["products"]

	body = ""
	statusCode = 200

	authorizer_response = event

	#print("EVENT", json.dumps(event))

	#Event is the response returned by the authorizer
	user_google_id = authorizer_response["requestContext"]["authorizer"]["user_id"]
	user_name = authorizer_response["requestContext"]["authorizer"]["user_name"]
	workspaceId = authorizer_response["pathParameters"]["workspaceId"]

	patched_info = json.loads(authorizer_response["body"])

	print ("body", patched_info)

	print("workpace id", workspaceId)
	#Then find the workspaces for this user
	cursor = workspace_collection.find({"_id": ObjectId(workspaceId)})

	#if workspace not found
	if (cursor.count() == 0):
		statusCode = 404
		body = {"Error":"Workspace does not exist!"}
	else:
		#Update the ones that were passed into POST request with correct data.
		for key in patched_info:
			#For MVP, assume everytime patch is called only adding one product
			if (key == "product"):
				print("key bitch")
				#Check to see if the url given exists in db, if not add
				check_for_product = check_product_exists(patched_info[key])
				product_id = check_for_product
				print("check", check_for_product)
				if (not check_for_product):
					product_id = add_product_amazon(patched_info[key])
					#Add to products array
				
				workspace_collection.update({"_id": ObjectId(workspaceId)}, {"$push": {"products": product_id}})
			else:
				workspace_collection.update_one({"_id": ObjectId(workspaceId)}, {"$set": {key:patched_info[key]}}, True)
		body = {"Message": "Success"}

	response = {
		"statusCode": statusCode,
		"body": json.dumps(body),
		"headers": {
			"Access-Control-Allow-Origin": "*"
		}
	}

	return response