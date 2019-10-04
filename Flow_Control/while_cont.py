while True:
    print ('What is yor name ?')
    name = input()
    if name != 'Jane':
        continue
        print('Hello, Jane. Is your password jannie ?')
        password = input()
        if password == 'jannie':
            break
        print('Access granted')
