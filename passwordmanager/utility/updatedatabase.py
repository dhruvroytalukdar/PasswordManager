import sqlite3
import getpass

def updateData():
    connection = sqlite3.connect('passwordmanager.db')
    cursor = connection.cursor()

    try:
        website  = input('Enter the website where you want to change the password:')
        update = input('What do you want to update')
        if update == 'password':
            database_query = 'UPDATE Passwords SET password=? WHERE website=?'
            new_password = getpass.getpass()
            #print(new_password)
            cursor.execute(database_query,(new_password,website))
        elif update == 'username':
            database_query = 'UPDATE Passwords SET username=? WHERE website=?'
            new_username = input('Enter the new username')
            cursor.execute(database_query,(new_username,website))
        else:
            print('Service not available')
        
        connection.commit()

    except sqlite3.Error as error:
        print('ERROR :',error)
    
    finally:
        cursor.close()
        connection.close()
        print('Connection close successfuly')