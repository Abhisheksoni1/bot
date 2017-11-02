import cex_io
import bitoasis
import time
import settings
import threading

if __name__ == '__main__':
    b = bitoasis.BITOASIS(settings.BITOASIS_CLIENT_ID, settings.BITOASIS_CLIENT_SECRET,
                          settings.BITOASIS_CLIENT_USERNAME, settings.BITOASIS_CLIENT_PASSWORD)
    ci = cex_io.CEX_IO(settings.CEX_IO_USERNAME, settings.CEX_IO_API_KEY, settings.CEX_IO_API_SECRET)
    while True:
        buy_amount = settings.BITOASIS_BUY_AMOUNT
        sell_price = ci.get_sell_price()
        buy_price = b.get_buy_price()
        eth_used = buy_amount * buy_price
        sell_amount = sell_price/eth_used
        per_change = (float(sell_price - buy_price)/sell_price)*100
        print("Sell Price is ${} \t Buy Price is ${} \t".format(sell_price, buy_price))
        print("Percentage change in prices are {} %".format(per_change))
        if per_change > settings.PER_CHANGE:
            # place a buy and sell order in both exchanges
            threading.Thread(target=b.place_buy_order, kwargs=({'amount': buy_amount, 'price': buy_price})).start()
            threading.Thread(target=ci.place_sell_order, kwargs=({'amount': sell_amount, 'price': sell_price})).start()
        time.sleep(1)