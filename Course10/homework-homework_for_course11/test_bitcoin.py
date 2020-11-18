import unittest
import requests
from unittest.mock import patch
import json

from bitcoin import get_values_in_eur

class OurResponse(requests.Response):
   def json(self):
        return {'rates': {'eur': {'value': 100}}}

#create a requests.Response object with our data
def get_response():
    return OurResponse()

    # response = requests.Response()
    # response.status_code = 200
    # content = {'rates': {'eur': {'value': 100}}}
    # #encode the dict to json
    # response._content = json.dumps(content)

class TestBitcoin(unittest.TestCase):

#      @patch('btc', 'value')
#      def test_bitcoin(self, btc_exchange):
#          exchange_rate = get_rates()
  @patch('requests.get', return_value=get_response())
  def test_eur(self, get):
     actual_value = get_values_in_eur()
        #compare the value of the API with what we expect
     self.assertEqual(100, actual_value)








