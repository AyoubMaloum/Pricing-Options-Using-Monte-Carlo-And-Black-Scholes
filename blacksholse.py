import streamlit as st 


def app():
    import numpy as np 
    import scipy.stats as se


    import numpy as np 
    import pandas as pd 
    import yfinance as yf 
    import plotly.express as px
    import datetime as datetime
    from datetime import timedelta as timedelta
    from streamlit_option_menu import option_menu


    st.title("Pricing Options Using Black Scholes Merton 🎲")
    st.header("Pricing Options Calculator 📊")


    ticker = st.selectbox('Select Ticker',("AAPL","AMZN","GOOGL","META","MSFT"))
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    data = yf.download(ticker,start = start_date - timedelta(days=7) , end = end_date)

    button_clicked_plot = st.button("Price By Time Chart 📈", key="custom_button1", help="Show")

    # Check if the button is clicked
    if button_clicked_plot:
        st.write(data)
        fig = px.line(data,x=data.index,y=data['Adj Close'],title=ticker)
        st.plotly_chart(fig)



    def import_stock_data(ticker,start= start_date, end = end_date):
        spots = data['Adj Close']
        last_price = spots[-1]
        return last_price

    spot = import_stock_data(ticker)


    st.write("The spot price is : ",spot)
    call_put = st.selectbox("Call or Put",("Call","Put"))
    strike = st.number_input("Strike Price",step= 10,min_value=0)
    r = st.number_input("Discount Rate")
    sigma = st.number_input('Volatility')  #volatility
    T = st.number_input('Option Time') #maturity


    def d1(spot,strike,r,sigma,T):
        return (np.log(spot/strike)+(r+sigma**2/2)*T) / (sigma*np.sqrt(T))

    def d2(spot,strike,r,sigma,T):
        return d1(spot,strike,r,sigma,T) - sigma*np.sqrt(T)

    def call_value(spot,strike,r,sigma,T):
        return spot*se.norm.cdf(d1(spot,strike,r,sigma,T)) - strike*se.norm.cdf(d2(spot,strike,r,sigma,T))*np.exp(-r*T)

    def put_value(spot,strike,r,sigma,T):
        return strike*se.norm.cdf(-d2(spot,strike,r,sigma,T))*np.exp(-r*T) - spot*se.norm.cdf(-d1(spot,strike,r,sigma,T))


    button_clicked = st.button("Simulate", key="custom_button3", help="Using Black Sholse")

    # Check if the button is clicked
    if button_clicked:
        if call_put == "Call":
            st.write("The call price is : ",call_value(spot,strike,r,sigma,T))
        else:
            st.write("The put price is : ",put_value(spot,strike,r,sigma,T))



    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)


    st.sidebar.success("Realised By Ayoub Maloum")