import requests

url = "http://172.105.87.133:3160/file"
# response = requests.get(url, header={'Content-type': 'application/json'})
#
# print(response)
# print(response.content)

response = requests.post(url, headers={'Content-type': 'application/json', 'fie_name': 'fisierul_lucatronlk'})
print(response)