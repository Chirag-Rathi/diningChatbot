import boto3
import json
import time

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('yelpRestaurants')

cuisines = ['Chinese','Indian','Japanese','Korean','Mexican']

for i in cuisines:
	f = open(i+'.json')
	data = json.load(f)
	for j in data:
		table.put_item(
			Item = 
			{
				'RestaurantId': str(j['id']),
				'RestaurantName': str(j['name']),
				'DisplayAddress': (j['location']['display_address']),
				'Coordinates': {
					str(j['coordinates']['latitude']),
					str(j['coordinates']['longitude'])
				},
				'NumberofReviews': str(j['review_count']),
				'Rating': str(j['rating']),
				'ZipCode': str(j['location']['zip_code']),
				'InsertTime': str(time.time())
			}
		)
	f.close()
