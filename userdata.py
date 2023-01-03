import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="onlinerest"
)

mc = db.cursor() 

def login(email, password):
    mc.execute(f"SELECT password FROM users WHERE email = '{email}'")
    detail = mc.fetchall()
    for i in detail:
        passw = detail[0][0]
    if passw == password:
        return True
    else:
        return False
    
def signup(email, name, address ,phnumber,sign_password):
    pz = ''
    mc.execute(f"INSERT INTO users (user_id,email, name, password, address, phonenumber) VALUES (DEFAULT, '{email}','{name}', '{sign_password}', '{address}', '{phnumber}')")
    # mc.execute(f"INSERT INTO USER (USER_ID, USER_NAME, PASSWORD) VALUES ('{id}', '{name}','{password}') ")
    db.commit()
    return True

def get_details(email):
    mc.execute(f"SELECT name, address, phonenumber FROM users WHERE email = '{email}'")
    details = mc.fetchall()
    # detail = []
    # for i in details:
    #     detail.append(i)
    return [details[0][0], details[0][1], details[0][2]]