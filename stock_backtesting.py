# https://www.backtrader.com/docu/
# https://wendys.tistory.com/173 pandas로 종목명 읽어오기
# finance data reader : https://financedata.github.io/posts/finance-data-reader-users-guide.html
# 시스템 트레이딩을 위한 데이터 사이언스
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web 
import yfinance as yf
import backtrader as bt

from datetime import datetime
from openpyxl import load_workbook

class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


cerebro = bt.Cerebro()  # create a "Cerebro" engine instance

# Create a data feed
data = bt.feeds.YahooFinanceData(dataname='078930.KS',
                                 fromdate=datetime(2007, 1, 1),
                                 todate=datetime(2020, 10, 1))
cerebro.broker.setcash(10000000.0)
cerebro.adddata(data)  # Add the data feed

cerebro.addstrategy(SmaCross)  # Add the trading strategy
cerebro.run()  # run it all
cerebro.plot()  # and plot it with a single command
