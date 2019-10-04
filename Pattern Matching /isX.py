#! /usr/bin/python3.6

while True:
    print('What is your age ?')
    age  = input()
    if age.isdecimal():

        break
    print('Please enter a number for your age. ' + str(type(age)))

while True:
    print('Choose a new password (letters and numbers only)')
    password = input()
    if password.isalnum() and len(password) > 4:
        break
    print('Password must contain leters and numbers only and not less than 4 characters')
