import requests
import json

# response = requests.get(' https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf')
# file_content = response.content
#
# with open('children_book.pdf', mode='bw') as file:
#     file.write(file_content)

url_info = 'http://api.open-notify.org/astros.json'
response = requests.get(url_info)
info_content = response.json()
with open('astronauts.json', mode='w') as file:
    json.dump(info_content, file, indent=4)

with open('astronauts.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
with open('astronauts.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
