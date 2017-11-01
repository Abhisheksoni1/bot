import hashlib
import hmac
from urllib import urlencode
import requests
import json
import time


class CEX_IO(object):
    BASE_URL = "https://cex.io/api/"
    username = ''
    api_key = ''
    api_secret = ''
    nonce_v = ''

    def __init__(self, username, api_key, api_secret):
        self.last_price = 0
        self.currency_1 = "ETH"
        self.currency_2 = "USD"
        self.trading_fee = 0.2
        self.sell_price = 0
        self.username = username
        self.api_key = api_key
        self.api_secret = api_secret

    # get timestamp as nonce
    def __nonce(self):
        self.nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
        return self.nonce_v

    # generate segnature
    def __signature(self):
        string = self.nonce_v + self.username + self.api_key  # create string
        signature = hmac.new(self.api_secret, string,
                             digestmod=hashlib.sha256).hexdigest().upper()  # create signature
        return signature

    def place_sell_order(self, **params):
        url = self.BASE_URL + "place_order/{}/{}".format(self.currency_1, self.currency_2)
        params.update({
            'key': self.api_key,
            'signature': self.__signature(),
            'nonce': self.__nonce(),
            'type': "sell"})
        params = urlencode(params)
        ret = requests.post(url, params).text
        data = json.loads(ret)
        if data.get("error", "") != "":
            print("Problem in placing order {}".format(data['error']))
        else:
            print("Order Detail is {}".format(data))

    def get_sell_price(self):
        ret = requests.get(self.BASE_URL + "tickers/{}/{}".format(self.currency_1, self.currency_2))
        data = json.loads(ret.text)
        for item in (data['data']):
            if item['pair'] == "ETH:USD":
                self.sell_price = item['bid']
        return self.sell_price

    def get_last_price(self):
        return self.last_price

    def update_last_price(self):
        ret = requests.get(self.BASE_URL + "last_price/{}/{}".format(self.currency_1, self.currency_2))
        data = json.loads(ret.text)
        self.last_price = float(data['lprice'])

if __name__ == '__main__':
    ci = CEX_IO("user", "api", "secret")
    ci.place_sell_order(amount=0.01, price=6100)