import json
from consumption import ConsumptionBelow100, ConsumptionBelow200, ConsumptionBelow300, ConsumptionAbove300

class Bill:
    #define the constructor
    def __init__(self, name, consumption):
        self.name = name
        self.consumption = consumption

class ConsumptionRepository:
    def get(self):
        bills = self.read_from_file()
        consumption_objects = []
        for bill_dict in bills:
            # create an object consumption
            new_consumption = self.make_consumption(bill_dict['consumption'], bill_dict['name'])
            # add a consumption object to the list
            consumption_objects.append(new_consumption)
        return consumption_objects

    def make_consumption(self, units, name):
        units = int(units)
        if units < 100:
            return ConsumptionBelow100(units, name).get_price()
        if units < 200:
            return ConsumptionBelow200(units, name).get_price()
        if units < 300:
            return ConsumptionBelow300(units, name).get_price()
        return ConsumptionAbove300(units, name).get_price()

    def read_from_file(self):
        # create a file object ( handler )
        file = open('electricity_bills.json')
        # read the content of the file, we get the string
        encoded_json = file.read()
        file.close()
        # decode the json
        bills = json.loads(encoded_json)
        return bills


#creat an object repository
repo = ConsumptionRepository()
bills = repo.get()
print(bills)