import sqlite3

try:
    connection = sqlite3.connect('passwordmanager.db')
    cursor = connection.cursor()

    # ***** CREATING A TABLE *****
    # create_table = '''
    #     CREATE TABLE Passwords (
    #         id INTEGER PRIMARY KEY,
    #         website VARCHAR(50),
    #         username VARCHAR(50) NOT NULL,
    #         password VARCHAR(50) NOT NULL
    #     );        
    # '''

    # *****RETRIEVING DATA FROM THE DATABASE TABLE ***** 
    # while True:
    #     website = input('Enter the website name:')
    #     username = input('Enter the username:')
    #     password = input('Enter the password:')

    #     insert_query = '''
    #         INSERT INTO Passwords (website, username, password)
    #         VALUES (?,?,?);
    #     '''

    #     cursor.execute(insert_query,(website,username,password))
    #     connection.commit()

    #     ch = input('Wanna quit? :')
    #     if ch == 'q':
    #         break

    # print('Values saved without any error')

    # *****RETRIEVING AND DISPLAYING DATA *****
    # command = 'SELECT * FROM Passwords'
    # cursor.execute(command)
    # records = cursor.fetchall()
    # print(f"Total {len(records)} records are fetched form the database.")
    # for key,website, username, password in records:
    #     print(f"Website: \'{website}\' Username: \'{username}\' Password: \'{password}\'")

except sqlite3.Error as error:
    print('Error while creating database table',error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print('Database closed successfully')
