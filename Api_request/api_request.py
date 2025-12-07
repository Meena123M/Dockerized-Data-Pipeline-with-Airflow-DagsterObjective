# import pandas as pd
from alpha_vantage.timeseries import TimeSeries



api_key='2IQOQ8070S69QSSN'

ticker='AAPL'

ts=TimeSeries(key=api_key,)

#get daily stocks
data,meta_data=ts.get_daily(symbol=ticker,outputsize='compact')

print(data)

# fetch data using function
def fetch_daily_stock_data(ticker_symbol):
    ts = TimeSeries(key=api_key,)
    data, meta_data = ts.get_daily(symbol=ticker_symbol, outputsize='compact')
    return data







