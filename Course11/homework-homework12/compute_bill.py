from bills_repository import ConsumptionRepository




#creat an object repository
repo = ConsumptionRepository()
bills = repo.get()


def compute_price(consumption):
    return consumption.name + ' has to pay ' + str(consumption.get_price()) + '$'


#print(bills)
#go throught all the dicts and compute the price
# for bill in bills:
#     #access the value, make it int
#     print(compute_price(bill))