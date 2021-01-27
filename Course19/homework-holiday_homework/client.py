import requests

# response = requests.get('http://localhost:8000')
#
# print(response)
# print(response.content)

data = {'type': 'Tulip', 'color': 'red', 'number': 8}

requests.post('http://localhost:8000', data)