import requests
import json


class BITOASIS(object):
    CONTANT = 3.6727299
    BASE_URL = "https://api.bitoasis.net/v1/exchange/"

    def __init__(self):
        self.buy_price = 0
        self.currency_1 = "ETH"
        self.currency_2 = "AED"
        self.trading_fee = 0.5
        self.last_price = 0

    def get_buy_price(self):
        url = self.BASE_URL + "ticker/{}-{}".format(self.currency_1, self.currency_2)
        data = json.loads(requests.get(url).text)['ticker']
        # print(data)
        self.buy_price = float(data['ask'])/self.CONTANT
        return self.buy_price

    def place_buy_order(self, **params):
        values = "{'side':'buy','type':'limit','pair':'{}-{}','amount':{},'price': {}}".\
            format(self.currency_1, self.currency_2, params['amount'], params['price'])
        headers = {
            'Content-Type': 'application/json'
        }
        url = self.BASE_URL + "order"
        ret = requests.post(url, values, headers).text
        print(ret)


b = BITOASIS()
b.place_buy_order(amount=0.1, price=6100)