from bills_repository import BillRepository
from consumption import ConsumptionBelow100, ConsumptionBelow200, ConsumptionBelow300, ConsumptionAbove300


def compute_bill(units):

    if units < 100:
        return ConsumptionBelow100(units).get_price()
    if units < 200:
        return ConsumptionBelow200(units).get_price()
    if units < 300:
        return ConsumptionBelow300(units).get_price()
    return ConsumptionAbove300(units).get_price()


#creat an object repository
repo = BillRepository()
bills = repo.get()


def compute_price(bill):
    consumption = int(bill.consumption)
    price = compute_bill(consumption)
    return bill.name + ' has to pay ' + str(price) + '$'


#print(bills)
#go throught all the dicts and compute the price
# for bill in bills:
#     #access the value, make it int
#     print(compute_price(bill))