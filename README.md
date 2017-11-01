# bot
Details of the project:

- Basic Arbitrage Trading Bot
- Only two exchanges, CEX.io and Bitoasis.net, for now ETH coins only. ETH will be deposited on CEX for selling
- Works through APIs
- Monitor BitOasis buy price and CEX sell price, monitor amount of ETH for buy and sell.
- When difference is above 1%, initiate trading. Buying from Bitoasis, selling on CEX.
 (price on Bitoasis is in AED, divide with 3.6727299 to get price in $ and add 0,5% for trading fee.
   Price on CEX is in $, add 0,2% for trading fee)
- Buy and sell should happen at same time
- Do buy/sell in smaller portions to avoid price mismatch (not enough of ETH for sell)


You can check our API
http://docs.bitoasis.apiary.io/#reference/exchange

You'll need to be signed in to access this link:
https://bitoasis.net/en/account.settings/api-settings
