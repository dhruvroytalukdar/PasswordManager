import sqlite3
import os

def createDatabase():

    try:
        connection = sqlite3.connect('passwordmanager.db')
        cursor = connection.cursor()

        #***** CREATING A TABLE *****
        create_table = '''
            CREATE TABLE Passwords (
                id INTEGER PRIMARY KEY,
                website VARCHAR(50),
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL
            );        
        '''
        cursor.execute(create_table)
        connection.commit()

    except sqlite3.Error as error:
        print('Error while creating database table',error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print('Database closed successfully')
