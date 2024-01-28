# Import the necessary Libraries for this app

import streamlit as st
import yfinance as yf
import pandas as pd

# Set the Page Layout
st.set_page_config(page_title='Stock Valuation App',layout='wide')

# Set title of the page 
st.title("Stock Valuation Tool")

# Side Bar for the user input

# Sidebar for user input
st.sidebar.header('User Input')

# Input for stock symbol
symbol = st.sidebar.text_input('Enter Stock Symbol:', 'AAPL')

# Input for valuation parameters
discount_rate = st.sidebar.slider('Discount Rate (%)', 0.1, 10.0, 5.0)
future_growth_rate = st.sidebar.slider('Future Growth Rate (%)', 0.1, 10.0, 5.0)

# Fetch historical stock prices
@st.cache
def get_stock_data(symbol):
    stock_data = yf.download(symbol, start='2022-01-01', end='2024-01-01')
    return stock_data

stock_prices = get_stock_data(symbol)

# Display historical stock prices
st.subheader(f'Historical Stock Prices for {symbol}')
st.line_chart(stock_prices['Close'])

# Valuation Calculation
st.subheader('Stock Valuation Calculation')

# Basic Valuation Formula (you can replace this with your preferred method)
discounted_cash_flow = stock_prices['Close'] * (1 + future_growth_rate / 100) / (1 + discount_rate / 100)
present_value = discounted_cash_flow.sum()

st.write(f'The present value of future cash flows is: ${present_value:.2f}')

# Additional features and calculations can be added as needed

# Disclaimer
st.sidebar.markdown('***Disclaimer: This is a basic example and not financial advice. Do your own research before making investment decisions.***')





