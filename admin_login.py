import streamlit as st 
from userdata import get_user_data, get_order_data, get_orderitem_data, get_orderitem_detail
import pandas as pd 
import asyncio 

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()



    

def user_data_table():
    df = pd.DataFrame(get_user_data())
    return df



def show_main_page():
    with mainSection:
        st.header('Admin Panel ')
        
        user, orders = st.tabs(['Users', 'orders' ])
        
        with user:
            hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                thead tr th: {display:none}
                </style> """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.subheader('user data display')
            s = user_data_table()
            st.table(s)
                
            
        with orders:
            st.subheader('order data display')
            hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                thead tr th: {display:none}
                </style> """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            order_df = pd.DataFrame(get_order_data())
            st.table(order_df)    
            st.subheader('Select the order id you want to get information of')
            ode_id = st.number_input(label="", min_value=1 )
            # st.button("Get Item Detail ", on_click=get_orderitem_detail_ad, args=(ode_id))
            orderitem_pd = pd.DataFrame(get_orderitem_detail(ode_id))
            st.table(orderitem_pd)



def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)




def LoggedIn_Clicked(email_id, password):
    if email_id == 'admin' and password == 'admin':
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False;
        st.error("Invalid user name or password")
        
        
        
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            st.subheader('Login Here 🎉')         
            email_id = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (email_id, password))
        


with headerSection:
    st.title("Online Food Ordering System  - Admin Login ")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()
        else:
            show_login_page()