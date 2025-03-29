import requests

link = 'https://dummyjson.com/users'

params = {
    'limit': 3000,
    'skip': 0
}

response = requests.get(link, params=params)
response_json = response.json()

users_link = response_json['users']

who_lives_in_san_francisco = 0
green_eyed_females_count = 0
users_under_of_30 = 0
for user in users_link:
    if user['age'] < 30:
        users_under_of_30 += 1

    if user['gender'] == 'female' and user['eyeColor'] == 'Green':
        green_eyed_females_count += 1

    if 'San Francisco' in user['address']['city']:
        who_lives_in_san_francisco += 1

pass
