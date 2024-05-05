import pandas as pd

from pycoingecko import CoinGeckoAPI

def getTokenPricedata(tokenid):
    cg = CoinGeckoAPI()


    ohlc = cg.get_coin_ohlc_by_id(id = tokenid, vs_currency = 'usd', days = '90')
    print (ohlc)

    pricedata_df = pd.DataFrame(ohlc)



    pricedata_df.columns = ["date", "open", "high", "low", "close"]

    return pricedata_df