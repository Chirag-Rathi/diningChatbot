import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
	TableName = 'yelpRestaurants',
	KeySchema = [
		{
			'AttributeName': 'RestaurantId',
			'KeyType': 'HASH'
		}
	],
	AttributeDefinitions = [
		{
			'AttributeName': 'RestaurantId',
			'AttributeType': 'S'
		}
	],
	ProvisionedThroughput = {
    	'ReadCapacityUnits': 5,
    	'WriteCapacityUnits': 5
	}
	)

table.wait_until_exists()

print(table.item_count)
