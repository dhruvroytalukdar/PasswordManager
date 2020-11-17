import sqlite3
import getpass

def insertData():
    try:
        connection = sqlite3.connect('passwordmanager.db')
        cursor = connection.cursor()

        #*****RETRIEVING DATA FROM THE DATABASE TABLE ***** 
        website = input('Enter the website name:')
        username = input('Enter the username:')
        password = getpass.getpass()
        

        insert_query = '''
            INSERT INTO Passwords (website, username, password)
            VALUES (?,?,?);
        '''

        cursor.execute(insert_query,(website,username,password))
        connection.commit()

    except sqlite3.Error as error:
        print('Error while creating database table',error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print('Database closed successfully')
