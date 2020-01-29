from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

client = boto3.resource('dynamodb',aws_access_key_id='AKIARISVIKVDXLIK4ORO', aws_secret_access_key='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', region_name='us-east-2')


# dynamodb.delete_table(TableName='movies3')
table = client.Table('Movies')

with open("moviedata.json") as json_file:
	movies = json.load(json_file, parse_float = decimal.Decimal)
	for movie in movies:
		year = int(movie['year'])
		title = movie['title']
		info = movie['info']

		print("Adding movie:", year, title)

		response = table.put_item(
			Item={
				'year': year,
				'title': title,
			}
		)