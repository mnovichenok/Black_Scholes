import numpy as np
from scipy.stats import norm
import yfinance as yf
from datetime import datetime
from datetime import date


class MarketDataFetcher:

    def __init__(self, ticker, expiry, strike):
        self.ticker = ticker
        self.expiry = expiry
        self.strike = strike

    def stock_price(self):
        stock = yf.Ticker(self.ticker)
        price = round(stock.history(period="1d", interval="1m")["Close"][-1], 2) #most recently closed stock price, rounded to 2 decimals
        return price

    def time_to_maturity(self):
        today = date.today()
        expiry_date = datetime.strptime(self.expiry, "%Y-%m-%d").date()
        delta_days = (expiry_date - today).days
        return delta_days/365.0

    def historical_volatility(self, window=30):
        #annulized volatility = standard deviation * √(252)
        stock = yf.Ticker(self.ticker)
        history = stock.history(period=f"{window}d")
        log_returns = np.log(history["Close"]/history["Close"].shift(1))
        return np.std(log_returns.dropna()) * np.sqrt(252)



class BlackScholes:
    def __init__(self, S, K, T, sigma, r, option_type):
        self.S = S
        self.K = K
        self.T = T
        self.sigma = sigma
        self.r = r
        self.option_type = option_type.lower()

    def d1(self):
        return (np.log(self.S / self.K) + (self.r + self.sigma*self.sigma/2) * self.T)/(self.sigma * np.sqrt(self.T))

    def d2(self):
        d1 = self.d1()
        return d1 - (self.sigma * np.sqrt(self.T))

    def call(self):
        return self.S * norm.cdf(self.d1()) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())

    def put(self):
        return self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2()) - self.S * norm.cdf(-self.d1()) 


