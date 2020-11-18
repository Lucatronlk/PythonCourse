# https://api.coingecko.com/api/v3/exchange_rates
# compute the exchange rate of bitcoin in eur and usd
# write tests for the compute function mocking the API
import requests
import json
import unittest
from unittest.mock import patch


# def get_bitcoin():
#     encoded_json = requests.get('https://api.coingecko.com/api/v3/exchange_rates').json()
#     print(encoded_json)
#     return encoded_json


def main():

    #call the coingeko for exchange rates
    response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')

    #print_the_object, see the response code
    print(response)
    #print the json
    #print(response.json())

    #print the BTC/EUR/USD info
    #save the json in an variable
    values = response.json()
    btc = (values['rates']['btc'])
    eur = (values['rates']['eur'])
    usd = (values['rates']['usd'])

    #compute

    print('1BTC is ' + str(eur['value']) + eur['unit'])
    print('1BTC is ' + str(usd['value']) + usd['unit'])

def get_values_in_eur():
    response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')
    values = response.json()
    eur = (values['rates']['eur'])
    return eur['value']


main()

    # print(get)

     # response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')
     # encoded_json = response.json()
     # print(encoded_json)


#     btc_rates = encoded_json.json['rates']['btc']
#     usd_rates = encoded_json.json['rates']['usd']
#     eur_rates = encoded_json.json['rates']['eur']
#
# print(btc_rates)

# def get_rates(coin_name, value):
#     # for coin in get_bitcoin():
#     #      if coin_name == coin["btc"] and coin_name == coin["eur"] and coin_name == coin["usd"]:
#     #          return coin["value"]



