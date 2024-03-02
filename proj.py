import streamlit as st 
import numpy as np 
import pandas as pd 
import yfinance as yf 
import plotly.express as px
import datetime as datetime
from datetime import timedelta as timedelta
from streamlit_option_menu import option_menu



selected = option_menu(
    menu_title= None,
    options = ["Monte Carlo","Black Sholse","Theorical"],
    icons=["house","book","envelope","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

#if selected == "Home":
 #   st.title(f"You have selected {selected}")
#if selected == "Projects":
#    st.title(f"You have selected {selected}")
#if selected == "Contact":
 #   st.title(f"You have selected {selected}")




st.title("Monte Carlo Simulation Using Brownian Motion 🎰")
st.header("Pricing Options Calculator 🔢")




ticker = st.sidebar.selectbox('Select Ticker',("AAPL","AMZN","GOOGL","META","MSFT"))
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')


data = yf.download(ticker,start = start_date - timedelta(days=7) , end = end_date)


button_clicked_plot = st.sidebar.button("Price By Time Chart 📈", key="custom_button1", help="Show")

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
nSimulation = st.number_input('Simulation Number',step = 100,min_value = 0)  #simulation_number
#spot = st.number_input('Spot Price',step = 10,min_value = 0) #strike price
strike = st.number_input('Strike Price',step = 10,min_value = 0) #strike price
sigma = st.number_input('Volatility')  #volatility
r = st.number_input('Discount Rate') #Discount Rate
#nSteps = st.number_input('Number of days',step = 1, min_value = 1)  #days
nSteps = st.slider('Number of days',1,252)  #days
T = st.number_input('Option Time') #maturity
dt = T/nSteps



drift = (r - (sigma*sigma)/2)*dt
a = sigma * np.sqrt(dt)

# Let's make the random variable that follow the normal distribution

rv = np.random.normal(0,1,(nSimulation,nSteps))


matrix = np.zeros((nSimulation,nSteps))




matrix[:,0] = spot

# Let's apply the formula of S(t+1)

for i in range(1,nSteps):
    matrix[:,i] = matrix[:,i-1]*np.exp(drift + a*rv[:,i])



# Let's calculate the payoff of call for every simulation

c = matrix[:,-1] - strike



# We can not take the negative one

for i in range(0,nSimulation):
    if(c[i]<0):
        c[i] = 0
        
#c

# Let's calculate the payoff of put for every simulation

p = strike - matrix[:,-1]
#p


# We can not take the negative one

for i in range(0,nSimulation):
    if(p[i]<0):
        p[i] = 0
        
#p


# Let's calculate the payoff of the call
call_payoff = np.mean(c)
#print("The call payoff is: ", np.mean(c))

# Let's calculate the payoff of the put
put_payoff = np.mean(p)
#print("The put payoff is: ", np.mean(p))


# Discounting back to today's price (provide the present value of a future value)
call_price = call_payoff * np.exp(-r*T)

put_price = put_payoff * np.exp(-r*T)


button_clicked = st.button("Simulate", key="custom_button", help="Using Brownian Motion")

# Check if the button is clicked
if button_clicked:
    if call_put == "Call":
        st.write("The call price is : ",call_price)
    else:
        st.write("The put price is : ",put_price)


# Simulating using np array
St = np.exp(
        (r - sigma ** 2 / 2 ) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size = (nSimulation,nSteps)).T
    )
    
St = np.vstack([np.ones(nSimulation), St])

St = spot * St.cumprod(axis=0)

time = np.linspace(0, T, nSteps+1)

tt = np.full(shape=(nSimulation, nSteps+1), fill_value=time).T

button_clicked_sim = st.button("Show Graph", key="custom_button2", help="Graph")

# Check if the button is clicked
if button_clicked_sim:
    st.subheader("Generated Graph")
    st.line_chart(St, use_container_width=True)



st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)


st.sidebar.success("Realised By Ayoub Maloum")
