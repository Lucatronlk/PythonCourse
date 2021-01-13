from stocks import TeslaStock, MicrosoftStock
from broker import Broker

tesla = TeslaStock()
sector = tesla.get_sector()
print(sector)
website = tesla.get_website()
print(website)
price = tesla.get_price()
print(price)

bill = MicrosoftStock()
sector = bill.get_sector()
print(sector)
website = bill.get_website()
print(website)
price = bill.get_price()
print(price)

broker = Broker([tesla, bill])
broker.save()

