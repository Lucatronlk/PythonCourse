import requests


url = 'http://localhost:8000/hello'
response = requests.get(url)

print(response)
print(response.content)


url_post = "http://localhost:8000/file"

data = {'file_name': 'myfile_luca'}
headers = {'file_name': 'fisier_luca'}
response = requests.post(url_post, data, headers=headers)


