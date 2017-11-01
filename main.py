import cex_io
import bitoasis
import time
import settings

if __name__ == '__main__':
    b = bitoasis.BITOASIS()
    ci = cex_io.CEX_IO(settings.CEX_IO_USERNAME, settings.CEX_IO_API_KEY, settings.CEX_IO_API_SECRET)
    while True:
        sell_price = ci.get_sell_price()
        buy_price = b.get_buy_price()
        per_change = (float(sell_price - buy_price)/sell_price)*100
        print("Sell Price is ${} \t Buy Price is ${} \t".format(sell_price, buy_price))
        print("Percentage change in prices are {} %".format(per_change))
        time.sleep(1)