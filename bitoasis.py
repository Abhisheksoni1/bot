import requests
import json
from urllib import urlencode


class BITOASIS(object):
    CONTANT = 3.6727299
    BASE_URL = "https://api.bitoasis.net/v1/exchange/"

    def __init__(self, client_id, client_secret, username, password):
        self.buy_price = 0
        self.currency_1 = "ETH"
        self.currency_2 = "AED"
        self.trading_fee = 0.5
        self.last_price = 0
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password

    def get_buy_price(self):
        url = self.BASE_URL + "ticker/{}-{}".format(self.currency_1, self.currency_2)
        data = json.loads(requests.get(url).text)['ticker']
        # print(data)
        self.buy_price = float(data['ask'])/self.CONTANT
        return self.buy_price

    def login(self):
        data = {
            'grant_type': "password",
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password
                }
        url = "https://api.bitoasis.net/v1/access_token"
        value = urlencode(data)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        ret = requests.post(url, data=value, headers=headers)
        print(ret.status_code)
        data = json.loads(ret.text)
        print data

    def place_buy_order(self, **params):
        self.login()
        value = json.dumps({
            'side': 'buy',
            'type': 'limit',
            'pair': "-".join([self.currency_1, self.currency_2]),
            'amount': params['amount'],
            'price': params['price']
                  })
        headers = {
            'Content-Type': 'application/json'
        }
        url = self.BASE_URL + "order"
        ret = requests.post(url, data=value, headers=headers).text
        print(ret)


if __name__ == '__main__':
    b = BITOASIS("client_id", "secret", "username", "password")
    b.place_buy_order(amount=0.1, price=6100)