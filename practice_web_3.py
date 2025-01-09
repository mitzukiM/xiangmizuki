import requests

url = 'http://api.open-notify.org/astros.json'

params = {

}
response = requests.get(url, params=params)
response_json = response.json()

people_in_space = response_json['people']
human_in_iss = []

for human in people_in_space:
    if human['craft'] == 'ISS':
        human_name = human['name']
        human_in_iss.append(human_name)

pass
