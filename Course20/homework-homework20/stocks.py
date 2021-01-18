from yfinance_wrapper import YahooFinanceStock

class Stock:
    def __init__(self,data: YahooFinanceStock):
         self.data = data
        #self.data = YahooFinanceStock(name)


    def get_sector(self):
      return self.data.get_info().get_sector()


    def get_website(self):
      return self.data.get_info().get_website()


    def get_price(self):
        return self.data.get_info().get_price()

class MicrosoftStock(Stock):
    def __init__(self):
        #call the parent constructor
        super().__init__('MSFT')


class TeslaStock(Stock):
    def __init__(self):
        super().__init__('TSLA')






