import yfinance

#
# microsoft = yfinance.Ticker("MSTF")
#
# print(microsoft.info)

class YahooFinanceStock:
    #constructor
    def __init__(self, name):
       # create an object to communicate with the Yahoo API
       self.ticker = yfinance.Ticker(name)
       #we only initialize the variable without a value
       self.info = None


    def get_info(self):
        if not self.info:
            #if we do not have the variable we initialize it
          self.info = YahooFinanceStockInfo(self.ticker.info)
        return self.info



class YahooFinanceStockInfo:
    def __init__(self, dict_info):
      self.dict_info = dict_info

    def get_sector(self):
         return self.__get__value('sector')


    def get_website(self):
         return self.__get__value('website')

    def get_price(self):
        return self.__get__value('regularMarketPrice')


    def __get__value(self, key):

        try:
            #try to access the key
            return self.dict_info[key]
        except KeyError:
            #we get here if the key does not exists
            return key + ' info not available'

