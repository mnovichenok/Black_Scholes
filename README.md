# Black-Scholes Option Pricing Model
This project implements a **Black-Scholes option pricing model** using the **FastAPI** framework for backend processing and the **requests** library for client-side interaction. It supports real-time option pricing using live stock data via `yfinance`.

##Features
- Compute prices for European **call** and **put** options
- Use **real-time stock data** from Yahoo Finance via `yfinance`
- Estimate **historical volatility** using the standard deviation of log returns
- Validate inputs (e.g., ticker, expiration date)
- REST API via FastAPI
- Interactive frontend using Streamlit

## 🧮 How Volatility Is Calculated

Volatility \( \sigma \) is calculated from the past 30 days of historical closing prices using the formula:

\[
\sigma = \text{std}(\log(P_t / P_{t-1})) \times \sqrt{252}
\]

Where:
- \( P_t \): closing price at day \( t \)
- \( \log(P_t / P_{t-1}) \): daily **log return**
- \( 252 \): trading days per year

---

##Black-Scholes Formula

The price of a European call or put option is computed using:

###Call Option:
\[
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
\]

###Put Option:
\[
P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)
\]

Where:

| Symbol | Meaning |
|--------|---------|
| \( C, P \) | Call and put option prices |
| \( S \) | Current stock price |
| \( K \) | Strike price |
| \( T \) | Time to expiration (in years) |
| \( r \) | Risk-free interest rate |
| \( \sigma \) | Annualized volatility of the underlying stock |
| \( N(\cdot) \) | Cumulative distribution function (CDF) of the standard normal distribution |
| \( d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}} \) |
| \( d_2 = d_1 - \sigma \sqrt{T} \) |

---

##Black-Scholes Assumptions
- The stock price follows a **geometric Brownian motion** with constant volatility and drift
- No dividends are paid during the option’s life
- Markets are **frictionless**: no transaction costs or taxes
- The risk-free interest rate is constant
- Options are **European-style** (only exercisable at expiration)
- No arbitrage opportunities exist
