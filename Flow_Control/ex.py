name = 'Joe'
name = input('Who are you?\n')
while name != 'Joe':
    print("I\'m fine, thanks. Who are you?")
    name = input('Who are you?\n')
password = 'swordfish'
password = input('What is your fish password?\n')
if password != 'swordfish':
    print(f'Hello, {name}. What is your password?')
    password = input('What is your password?\n')
if name == 'Joe' and password == 'swordfish':
    print (f"Hello, {name}. Access granted")
# password = 'swordfish'
# if password != 'swordfish':
    # print(f"Hello, {name}. What is your password?")
    # password = input('What is your password?\n')
# else:
    # print('Access granted.')
