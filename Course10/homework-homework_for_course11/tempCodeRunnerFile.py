def get_month():
    i = 1
    while i < 30:
        date = '2020-10-' + str(i)
        response = requests.get('https://api.nasa.gov/planetary/apod',
                                params={'api_key': 'DEMO_KEY', 'date': date})
    print(response.json()['title'])
    i += 1


get_month()