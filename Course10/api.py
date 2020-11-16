import requests
import json
import unittest
from unittest.mock import patch


def get_iss():

     #response = requests.get('https://api.wheretheiss.at/v1/satellites')
     parameters = {"lat": 40.71, "lon": -74}
     response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
     raise Exception('message')

     print(response)
     print(response.status_code)
     return response['status_code']

     encoded_json = response.json()
     print(encoded_json)
     print(encoded_json['response'])
     json.loads(encoded_json)
    # decoded_json = json.loads(encoded_json)
    # print(decoded_json)
    # print(decoded_json['response'])

class TestIss(unittest.TestCase):
    # def test_error(self):
    #     with self.assertRaises(TypeError):
    #        get_iss()


    @patch('request.get', return_value={'status_code': 400})
    def test_iss(self, iss_call):
        response_code = get_iss()

        self.assertEqual(400, response_code)

