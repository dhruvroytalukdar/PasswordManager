from utility.createdatabase import createDatabase
from utility.display import displayData
from utility.insertdata import insertData
from utility.updatedatabase import updateData
import os

def creating_the_database():
    createDatabase()

def main():
    #key = input('Please enter the security key:')
    # if key != os.getenv('SECRET_KEY'):
    #     print('Sorry key is incorrect')
    while True:
        print('\nWhat do you want to do?')
        print('1.For inserting data.')
        print('2.Displaying the stored passwords.')
        print('3.Update an existing data.')
        val = input()

        if val == '1':
            insertData()
        elif val=='2':
            displayData()
        else:
            updateData()
        ch = input('Wanna quit?\n')
        if ch == 'q':
            break

if __name__ == '__main__':
    main()