import json

class StocksFile:
    def read(self):
        #open for read
        file = open('stocks.txt')
        content = file.read()
        file.close()
        dict = json.loads(content)
        return dict

    def write(self, dict):
        #encode the python dictionary to JSON, so we can write it to the file
        json_dict = json.dumps(dict)
        file = open('stocks.txt', 'w')
        file.write(json_dict)
        file.close()

# file = StocksFile()
# stocks = file.read()
# print(stocks)
# print(stocks['MSFT'])