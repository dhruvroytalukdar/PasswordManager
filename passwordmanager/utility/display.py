import sqlite3

def displayData():
    try:
        connection = sqlite3.connect('passwordmanager.db')
        cursor = connection.cursor()

        # *****RETRIEVING AND DISPLAYING DATA *****
        command = 'SELECT * FROM Passwords'
        cursor.execute(command)
        records = cursor.fetchall()
        print(f"Total {len(records)} records are fetched form the database.")
        print()
        for key, website, username, password in records:
            print(f"Website: \'{website}\' Username: \'{username}\' Password: \'{password}\'")
        print()

    except sqlite3.Error as error:
        print('Error while creating database table',error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print('Database closed successfully')
