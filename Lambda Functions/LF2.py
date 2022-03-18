import json
import boto3
import requests
from requests_aws4auth import AWS4Auth
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    tableName = 'yelpRestaurants'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('yelpRestaurants')
    client = boto3.client('sqs')
    dynamoClient = boto3.client('dynamodb')
    emailClient = boto3.client('ses')
    response = client.receive_message(
        QueueUrl='url'
        )
        
    emailDestination = {
        'ToAddresses': [
            'chiragrathi9101@gmail.com'
        ]
    }
    
    data = response['Messages'][0]['Body']
    data = json.loads(data)
    cuisine = str(data['Cuisine'])
    
    host = 'url'
    index = 'restauants'
    url = host+'/' + index + '/_search'
    
    query = {
        "size": 5,
        "query": {
            "multi_match": {
                "query": cuisine,
                "fields": ['Cuisine']
            }
        }
    }
    
    headers = {
	'Content-type': 'application/json'
    }
    
    r = requests.get(url, auth=('username', 'password'), data=json.dumps(query), headers = headers)
    print(r.json()['hits']['hits'][0]['_source']['RestaurantId'])
    
    Key = {
        'RestaurantId': r.json()['hits']['hits'][0]['_source']['RestaurantId']
    }
    
    dynamoDbResponse = table.get_item(Key=Key)
    
    emailMessage = {
        'Subject': {
            'Data': 'Restaurant Suggestions'
        },
        'Body': {
            'Text': {
                'Data': str(dynamoDbResponse)
            }
        }
    }
        
    res = emailClient.send_email(Source='chiragrathi9101@gmail.com',Destination=emailDestination,Message=emailMessage)
    
    response2 = client.delete_message(
        QueueUrl='url',
        ReceiptHandle=response['Messages'][0]['ReceiptHandle']
    )
