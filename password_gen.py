import sqlite3
import random

def create_table():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS accounts(NAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);')
    cursor.close()
    connection.close()

def store_password(name,password):
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO accounts(NAME,PASSWORD) VALUES(?,?);',(name,password))
    connection.commit()
    cursor.close()
    connection.close()

def display():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    list = cursor.execute('SELECT * FROM accounts')
    for i in list:
        print('\n\nAccount Name: ' + i[0])
        print('\nPassword: '+ i[1])
        print('---------------------')
    cursor.close()
    connection.close()

    

def generate(length):
    string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*~?'
    string_list = list(string)
    password = ''
    for i in range(length):
        password = password + str(string_list[random.randint(0,70)])
    return(password)

while(True):
    print('----RANDOM PASSWORD GENERATOR----')
    print('1.Generate\n2.Display\n3.Quit\n')
    choice = int(input('Enter the choice: '))
    if choice == 1:
        l = int(input('\nEnter the lenght of password: '))
        acc = input('\nEnter account name for the password: ')
        password = generate(l)
        print('Your generated password is for '+ acc +' is : ' + password)
        create_table()
        store_password(acc,password)
    elif choice == 2:
        display()
    else:
        exit()