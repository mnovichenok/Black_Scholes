import streamlit as st
import requests


st.title("Black-Scholes Option Pricer")

#user inputs
ticker = st.text_input("Stock Ticker")
K = st.number_input("Strike Price", min_value=0.0)
expiry = st.text_input("Expiration Date (YYYY-MM-DD)")
option_type = st.selectbox("Option Type", ["Call", "Put"])
r = st.slider("Risk-Free Rate", 0.0, 0.1)

if st.button("Calculate Option Price"):
    user_option = {
        "ticker": ticker,
        "K": K,
        "expiry": expiry,
        "option_type": option_type,
        "r": r
    }

    result = requests.post("http://localhost:8000/option/", json=user_option)

    if result.status_code == 200:
        price = result.json()["price"]
        S = result.json()["S"]
        T = result.json()["T"]
        sigma = result.json()["sigma"]
        name = result.json()["name"]
        
        st.success(f"{option_type} option price: ${price:.2f}")
        st.markdown(f"""
            **{name}**
            - Current Price (S): ${S:.2f}  
            - Strike Price (K): ${K}  
            - Time to Expiry (T): {T:.4f} years  
            - Volatility (σ): {sigma:.2%}  
            - Risk-Free Rate (r): {r:.2%}  
        """)
    else:
        #st.error(f"Error from API :  {result.status_code} — {result.text}")
        try:
            detail = result.json().get("detail", "Unknown error")
        
            if isinstance(detail, list):  # for validation errors
                detail = detail[0].get("msg", "Validation error")
        
        except Exception:
            # fallback if server didn't return JSON at all
            detail = result.text or "Server returned invalid response"
        
        st.error(f"API error ({result.status_code}): {detail}")
        
