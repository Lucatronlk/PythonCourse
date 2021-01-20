import requests


# url = 'http://localhost:8000/hello'
# response = requests.get(url)
#
# print(response)
# print(response.content)
#
#
# url_post = "http://localhost:8000/file"
#
# data = {'file_name': 'myfile_luca'}
# headers = {'file_name': 'fisier_luca'}
# response = requests.post(url_post, data, headers=headers)


# url_put = "http://localhost:8000/file"
# headers = {'file_name': 'fisier_luca', 'content': 'hello'}
# requests.put(url_put, headers=headers)


url_delete = "http://localhost:8000/file"
headers = {'file_name': 'fisier_luca'}
requests.delete(url_delete, headers=headers)
