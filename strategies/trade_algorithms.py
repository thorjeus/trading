import polo_api
#sell moneys
APIKey,Secret = polo_api.get_keys()
pol = polo_api.poloniex(APIKey,Secret)

def sell_moneys(moneys):
    #get what you've got
    #place all the orders
    #check if there are still here, if yes, moves them : does that mutltiple times
    #moves at a lower price : should sell immediatly (check after one second for instance)

def buy_moneys(moneys):
    #get what you've got ? (how many btc for instance)
    #place all the orders
    #check if there are still here, if yes, moves them : does that mutltiple times
    #moves at a higher price : should buy immediatly (check after one second for instance)

def compute_change(last_prices):
    ticker = pol.returnTicker()