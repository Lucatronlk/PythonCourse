import json

class Bill:
    #define the constructor
    def __init__(self, name, consumption):
        self.name = name
        self.consumption = consumption

class BillRepository:

    def get(self):
        # create a file object ( handler )
        file = open('electricity_bills.json')
        # read the content of the file, we get the string
        encoded_json = file.read()
        file.close()
        #decode the json
        bills = json.loads(encoded_json)
        bill_objects = []
        for bill_dict in bills:
            # create an object bill
            new_bill = Bill(bill_dict['name'], bill_dict['consumption'])
            # add a bill object to the list
            bill_objects.append(new_bill)

        return bill_objects

#creat an object repository
repo = BillRepository()
bills = repo.get()
print(bills)