import streamlit as st 



st.title("Monte Carlo")
st.header("Welcome to My Streamlit App")
st.write("""
    # Monte carlo simulation 
    It's the best way to have the price of the option
"""
         )

choosen = st.selectbox("Simulation",("Black Sholes","Brownian Motion","Monte Carlo"))
st.write(choosen)

st.sidebar.write("Select a method")
st.sidebar.selectbox("Simulwation",("Blackw Sholes","Brownwian Motion","Monwte Carlo"))