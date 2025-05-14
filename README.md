# Black-Scholes Option Pricing Model
This project implements a **Black-Scholes option pricing model** using the **FastAPI** framework for backend processing and the **requests** library for client-side interaction. It supports real-time option pricing using live stock data via **yfinance**.

## Features
- Computes prices for European **call** and **put** options
- Uses **real-time stock data** from Yahoo Finance via yfinance
- Estimates **historical volatility** using the standard deviation of log returns
- Validates inputs (e.g., ticker, expiration date)
- REST API via FastAPI
- Interactive frontend using Streamlit


## Annualized Volatility Calculation

Annualized volatility (σ) (standard deviation of returns)  is calculated from the past 30 days of historical closing prices using the formula:

### σ = stdev(ln(P<sub>t</sub> / P<sub>t-1</sub>)) × √(252)

Where:
- P<sub>t</sub> : closing price at day t
- log(P<sub>t</sub> / P<sub>t-1</sub>) : daily **log return**
- 252 : trading days per year



## Black-Scholes Formula

The price of a European call or put option is computed using:

![image](https://github.com/user-attachments/assets/1cb5de3f-d78b-44d9-82e2-5d47544bbde8)

Where:
- C, P : Call and put option prices
- S<sub>0</sub> : Current stock price
- K : Strike price
- T : Time to expiration (in years)
- r : Risk-free interest rate
- σ : Annualized volatility of the underlying stock
- N : Cumulative distribution function (CDF) of the standard normal distribution 

## Assumptions
- The stock price follows a **geometric Brownian motion** with constant volatility and drift
- No dividends are paid during the option’s life
- Markets are **frictionless**: no transaction costs or taxes
- The risk-free interest rate is constant
- Options are **European-style** (only exercisable at expiration)
- No arbitrage opportunities exist


### - Maya Novichenok
