import numpy as np
import datetime as dt
import pandas_datareader as pdr

def getData(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start=start, end=end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix


def portfolioPerformance(weights, meanReturns, covMatrix):
    returns = np.sum(meanReturns*weights)*252
    std = np.sqrt(
            np.dot(weights.T,np.dot(covMatrix, weights))
           )*np.sqrt(252)
    return returns, std

stocklist = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
# stocks=[stock for stock in stocklist]
# print(stocks)

weights = np.array([0.6, 0.1, 0.1, 0.1])

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365)
# print(getData(stocklist, startDate, endDate))

meanReturns, covMatrix=getData(stocklist, startDate, endDate)
returns, std = portfolioPerformance(weights, meanReturns, covMatrix)

print(round(returns*100,2), round(std*100,2))
