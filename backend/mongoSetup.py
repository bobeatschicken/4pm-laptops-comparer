import os
from pymongo import MongoClient

def connect_database():
	# Connect to MongoDB
	db_url = os.environ['DB_URL']
	print(f"Connecting to {db_url}")
	client = MongoClient(db_url)
	db = client.compurator
	print("connected to database")
	return db

def get_user_auth(event):
	# Get user info from authorizer
	authorizer_response = event
	print("requestContext: ", authorizer_response["requestContext"]["authorizer"])
	google_id = authorizer_response["requestContext"]["authorizer"]["user_id"]
	name = authorizer_response["requestContext"]["authorizer"]["user_name"]
	return {"g_id": google_id, "name": name}