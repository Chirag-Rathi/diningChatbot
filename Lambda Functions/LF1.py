import json
import boto3

def lambda_handler(event, context):
    slotsToComplete = ['Location','Cuisine','DiningTime','NumberOfPeople','PhoneNumber']
    
    sqs = boto3.client('sqs')
    queue_url = 'url'
    
    triggeredFlag = 0
    response = {}
    slots = event['currentIntent']['slots']
    intentName = event['currentIntent']['name']
    print(slots)
    
    for i in slotsToComplete:
        print(i)
        if i not in slots:
            triggeredFlag = 1
            response = {
            "dialogAction": {
                "type": "ElicitSlot",
                'intentName': intentName,
                "slots": slots, 
                "slotToElicit": i
                }
            }
            break
        
        elif not slots[i]:
            triggeredFlag = 1
            response = {
            "dialogAction": {
                "type": "ElicitSlot",
                'intentName': intentName,
                "slots": slots, 
                "slotToElicit": i
                }
            }
            break

    if(triggeredFlag==0 and i=='PhoneNumber'):
        
        res = sqs.send_message(
        QueueUrl=queue_url,
        MessageAttributes={
        'Location': {
            'DataType': 'String',
            'StringValue': slots['Location']
        },
        'Cuisine': {
            'DataType': 'String',
            'StringValue': slots['Cuisine']
        },
        'DiningTime': {
            'DataType': 'String',
            'StringValue': slots['DiningTime']
        },
        'NumberOfPeople': {
            'DataType': 'Number',
            'StringValue': slots['NumberOfPeople']
        },
        'PhoneNumber': {
            'DataType': 'Number',
            'StringValue': slots['PhoneNumber']
        }
    },
    MessageBody=(
        json.dumps(slots)
        ),
    MessageGroupId = '123432'
    )
        
        response = {
            "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
            "contentType": "PlainText",
            "content": "We will send you the recommendations shortly. Have a nice day"
            }
        }
    }
    return response
