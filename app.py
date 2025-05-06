import streamlit as st
from main import MarketDataFetcher, BlackScholes
from datetime import datetime

st.title("Black-Scholes Option Pricing Tool")


#user inputs
ticker = st.text_input("Stock Ticker")
K = st.number_input("Strike Price", min_value=0.0, value=1500.0)
expiry = st.text_input("Expiration Date (YYYY-MM-DD)")
option_type = st.selectbox("Option Type", ["Call", "Put"])
r = st.slider("Risk-Free Rate", 0.0, 0.1)


#calculate option price
if st.button("Calculate Option Price"):
    fetcher = MarketDataFetcher(ticker, expiry, K)
    S = fetcher.stock_price()
    T = fetcher.time_to_maturity()
    sigma = fetcher.historical_volatility()

    option = BlackScholes( S, K, T, sigma, r, option_type)
    if option_type == 'Call':
        price = option.call()
    else:
        price = option.put()

    st.success(f"{option_type} option price: ${price:.2f}")
    st.markdown(f"""
        **Inputs:**
         Current Price (S): ${S:.2f}  
         Strike Price (K): ${K}  
         Time to Expiry (T): {T:.4f} years  
         Volatility (σ): {sigma:.2%}  
         Risk-Free Rate (r): {r:.2%}  
    """)
