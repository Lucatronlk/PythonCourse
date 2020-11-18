# http://www.7timer.info/bin/astro.php
# parameter example: lon=113.2, lat=23.1, ac=0, unit=metric, output=json, tzshift=0
# Make a class with methods to find the weather in Timisoara, Bucharest, Oradea, Suceava
# Make 1 test for each method mocking the API

import requests
import json
import unittest
from unittest.mock import patch

#def get_weather():
parameters = {"lon": 113.2, "lat": 23.1, "ac": 0, "unit": 'metric', "output": json, "tzshift": 0 }
response = requests.get("http://www.7timer.info/bin/astro.php", params=parameters)
print(response)
#return response['status_code']
encoded_json = response.json()
decoded_json = json.loads(encoded_json)
print(decoded_json)



