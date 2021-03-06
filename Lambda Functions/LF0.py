import json
import boto3

client = boto3.client('lex-runtime')

def lambda_handler(event, context):
    
    response = client.post_text(
    botName='diningConcierge',
    botAlias='test',
    userId='abc',
    inputText=event['messages'][0]['unstructured']['text']
)
    # TODO implement
    return {
        'statusCode': 200,
        'messages': [{
            'type': 'unstructured',
            'unstructured': {
                'text': response['message']
            }
        }]
    }
