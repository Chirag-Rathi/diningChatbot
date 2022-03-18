from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import requests
import boto3
import json

host = 'url'
region = 'us-east-1'
cuisines = ['Chinese','Indian','Japanese','Korean','Mexican']

index = 'restauants'
typeVar = 'Restaurants'
service = 'es'

docObj = {
	"Restaurants": {
		"properties": {
			"RestaurantID": {
				"type": "text"
			},
			"Cuisines": {
				"type": "text"
			}
		}
	}
}

params = {
	'include_type_name': 'true'
}

headers = {
	'Content-type': 'application/json'
}

r = requests.put(host+'/'+index+'/'+typeVar+'/_mappings', auth=('username', 'password'), data=json.dumps(docObj), params = params, headers=headers)
