from fastapi import FastAPI
from pydantic import BaseModel
from black_scholes import MarketDataFetcher, BlackScholes
import requests

app = FastAPI()

class Option(BaseModel):
    ticker: str
    K: float
    expiry: str
    option_type: str
    r: float

@app.post("/option/")
def get_option(option: Option):
    fetcher = MarketDataFetcher(option.ticker, option.expiry, option.K)
    S = fetcher.stock_price()
    T = fetcher.time_to_maturity()
    sigma = fetcher.historical_volatility()

    model = BlackScholes( S, option.K, T, sigma, option.r, option.option_type)
    if option.option_type == 'Call':
        price = model.call()
    else:
        price = model.put()
    
    return {"price": price, "S": S, "T": T, "sigma": sigma}

