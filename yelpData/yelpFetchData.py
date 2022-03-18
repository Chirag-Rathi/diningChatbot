import json
import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "apiKey"

cuisines = ['Indian', 'Chinese', 'Japanese', 'Korean', 'Mexican']

header = {
	'Authorization': api_key
}

params = {
	'location': 'New York City',
	'category': 'Restaurants',
	'term': '',
	'limit':50,
	'offset': 0
}

for i in cuisines:
	res = []
	params['term'] = i
	j = 0
	while(j<1000):
		params['offset'] = j
		response = requests.get(url, headers=header, params = params).json()
		res.extend(response['businesses'])
		print(j)
		j += 50
	with open(i+'.json', 'w') as outfile:
		json.dump(res,outfile)

