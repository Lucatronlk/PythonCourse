# url: https://pokeapi.co/api/v2/pokemon/<pokemon_number>
# pokemon_number=1 will show results for bulbasaur
# url: https://pokeapi.co/api/v2/pokemon/<pokemon_name>
# make a class with 2 methods for each api calls
# write 3 tests which call the real API and 3 tests which mock the API
import requests
import json
import unittest
from unittest.mock import patch


class Pokemon:


  def get_by_number(self, number):
     response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(number))
     content = response.json()
     return content['species']['name']

# pokemon = Pokemon()
# content = pokemon.get_by_number(25)
# print(content)

   # def get_bulbasar(self):
   #   response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
   #   encoded_json = requests.get("https://pokeapi.co/api/v2/pokemon/1").json()
   #   print(encoded_json)
   #
   # def get_charmeleon(self):
   #    response_2 = requests.get("https://pokeapi.co/api/v2/pokemon/5")
   #    encoded_json_2 = requests.get("https://pokeapi.co/api/v2/pokemon/5").json()
   #    print(encoded_json_2)



# class Test_Pokemon_Api(unittest.TestCase):
#
#
#     @patch('request.get', return_value={'status_code': 200})
#     def test_bulbasar(self, bulbasar_call):
#          response_code = get_bulbasar()
#          self.assertRaises(200, response_code)

