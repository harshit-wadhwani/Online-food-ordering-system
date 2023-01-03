import streamlit as st 
from userdata import login, signup, get_details
import pandas as pd 

st.set_page_config(page_title='Order Food Now !', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()

   
food_list=[None, None, None ]
qty_list=[None, None, None ]
amt_list=[None, None, None]

# food_list=[]
# qty_list=[]
# amt_list=[]
order = {
    'Food Name':food_list,
    'Qty' : qty_list,
    'Amount':amt_list
}

cart = pd.DataFrame(order)

def show_main_page():
    with mainSection:
        st.header(f" Welcome {st.session_state['details'][0]} :sunglasses:")
        
        
        menu, cart = st.tabs(['Menu', 'Cart'])
        
        with menu:
            
            st.subheader('select the Food you want to order') 
            
            col1, col2, col3 = st.columns(3)
            col1.image('pizza.jpg')
            col1.text("Pizza 🍕")
            if col1.checkbox(label ='Order Pizza @ ₹199',key =1):
                col1.text('Enter QTY. -')
                c_pizza = col1.text_input(label="", value="0", placeholder="Enter Quantity", key = 79)
                food_list[0] = 'pizza'
                qty_list[0] = c_pizza
                amt_list[0] = int(c_pizza)*199
            
                
            
            col2.image('burger.jpg')
            col2.text("Burger 🍔")
            if col2.checkbox('Order Buger @ ₹99',key =2):
                col2.text('Enter QTY. -')
                c_burger = col2.text_input(label="", value="0", placeholder="Enter Quantity",key = 89  )
                
                food_list[1] = 'burger'
                qty_list[1] = c_burger
                amt_list[1] = int(c_burger)*99
            
                
                
            
            
            col3.image('noodles.jpg')
            col3.text("Noodles 🍜")
            if col3.checkbox('Order noodles @ ₹149',key =3):
                col3.text('Enter QTY. -')
                c_noodles = col3.text_input(label="", value="0", placeholder="Enter Quantity", key = 69)
                food_list[2] = 'noodles'
                qty_list[2] = c_noodles
                amt_list[2] = int(c_noodles)*149
                
            
                
                
            
            with cart:
                hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                 """
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                
                order = {
                        'Food Name':food_list,
                        'Qty' : qty_list,
                        'Amount':amt_list
                    }
                print(food_list)
                print(qty_list)
                print(amt_list)
                
                cart = pd.DataFrame(order)
                cart_final = cart.dropna()
                st.table(cart_final)
            
        # st.button("Order Your Items :tada: ", on_click=order)
        
        
         
                   
               
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    st.session_state['details'] = None
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
        

def LoggedIn_Clicked(email_id, password):
    if login(email_id, password):
        st.session_state['loggedIn'] = True
        st.session_state['details'] = get_details(email_id)
    else:
        st.session_state['loggedIn'] = False;
        st.session_state['details'] = None
        st.error("Invalid user name or password")
        
def signup_clicked(email, name, address ,phnumber,sign_password):
    try :
        if signup(email, name, address ,phnumber,sign_password):
            st.success("Signup successful ")
            st.balloons()
    except:
        st.warning('Invalid User ID or user ID already taken')
    
        
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            
            login, signup = st.tabs(["Login ✨", "Signup ❤️"])
            with login:
                st.subheader('Login Here 🎉')
                global userName           
                email_id = st.text_input (label="", value="", placeholder="Enter your user name")
                password = st.text_input (label="", value="",placeholder="Enter password", type="password")
                st.button ("Login", on_click=LoggedIn_Clicked, args= (email_id, password))
            with signup:
                st.subheader('Signup 🫶')
                email = st.text_input(label="", value="", placeholder = "Enter your Email-ID", key = 10)
                name = st.text_input (label="", value="", placeholder="Enter your Name", key =9)
                
                address = st.text_input(label="", value="", placeholder ="Enter your Address:", key = 13)
                
                phnumber = st.text_input(label= "", value="+91 ", placeholder ='Enter you Phone Number', key =14)
                
                sign_password =  st.text_input (label="", value="",placeholder="Enter password", type="password", key = 11)
                cnf_password =  st.text_input (label="", value="",placeholder="confirm your password", type="password", key = 12)
                st.button ("Sign UP", on_click=signup_clicked, args= (email, name, address ,phnumber,sign_password))
                if sign_password != cnf_password:
                    st.warning('Password does not match')


with headerSection:
    st.title("Online Food Ordering System 😋")
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