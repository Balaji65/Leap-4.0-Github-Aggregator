import json

print('Loading function')

def lambda_handler(event, context):
	#1. Parse out query string parameters
	repositoryId = event['queryStringParameters']['repositoryId']
	repsitorydate = event['queryStringParameters']['date']
	repositorysize = event['queryStringParameters']['size']

	print('repositoryId=' + repositoryId)
	print('repositorydate=' + repositorydate)
	print('repositorysize=' + repositorysize)

	#2. Construct the body of the response object
	repositoryResponse = {}
	repositoryResponse['repositoryId'] = 'manic'
	repositoryResponse['date'] = '10.07.2021'
	repositoryResponse['size'] = '20mb'
	repositoryResponse['message'] = 'Hello from manic'

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(repositoryResponse)

	#4. Return the response object
