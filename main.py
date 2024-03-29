import streamlit as st

from streamlit_option_menu import option_menu


import montecarlo, theoretical, blacksholse, contact
st.set_page_config(
        page_title="Pricing Options",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title=None,
                options=['Monte Carlo','Black-Scholes','Theoretical','Contact'],
                icons=['trophy-fill','trophy-fill','chat-fill','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#ff4b4b"},}
                
                )
#house-fill  person-circle  trophy-fill  chat-fill   info-circle-fill
        
        if app == "Monte Carlo":
            montecarlo.app()
        if app == "Black-Scholes":
            blacksholse.app()    
        if app == "Theoretical":
            theoretical.app()        
        if app == 'Contact':
            contact.app()
       
             
          
             
    run()            
         