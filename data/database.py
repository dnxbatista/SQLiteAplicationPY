import sqlite3
connectionsql = sqlite3.connect('data/customers.db')
conCursor = connectionsql.cursor()

def show_all():
    print('\n')
    print('--------------------------')
    conCursor.execute(f"SELECT rowid, * FROM customers ORDER BY rowid")
    items = conCursor.fetchall()
    for item in items:  
        print(item)    
    connectionsql.commit() #Send Commands
    continueInput = input('Pressione [ENTER] Para Continuar... ')
    print('\n')

def addNewItem(first_name,last_name,age,email):
    conCursor.execute(f"""
    INSERT INTO customers VALUES ('{first_name}','{last_name}','{age}','{email}')
    """)
    connectionsql.commit() #Send Commands

def updateItem(updateItemType,updateValue, id):
    conCursor.execute(f"""
        UPDATE customers SET '{updateItemType}' = '{updateValue}' WHERE rowid = {id}
    """)

def deleteItem(id):
    conCursor.execute(f"""
        DELETE FROM customers WHERE rowid = {id}
    """)

def disconnect():
    connectionsql.close() #Close Connection
