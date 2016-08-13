import time
import urllib2
from urllib2 import urlopen
from yahoo_finance import Share
from ticker_parse import tickers

def yahooStats(stock):
    try:
        # qs short for Query Stock
        qs = Share(stock)
        price_book = qs.get_price_book()
        if float(price_book) < 2:
            #print stock,'price to book ratio:', price_book
            peg_5_year = qs.get_price_earnings_growth_ratio()
            if 0 < float(peg_5_year) < 2:
                trailing_pe = qs.get_price_earnings_ratio()
                if float(trailing_pe) < 15:
                    print stock, 'meets requirements', 'p/b ratio', price_book,\
                    'P/E 5 year', peg_5_year , 'trailing P/E', trailing_pe

    except  Exception, e:
        print 'There is an error', str(e)

for stock in tickers:
    yahooStats(stock)
    time.sleep(.5)
