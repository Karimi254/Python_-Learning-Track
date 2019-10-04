#While infinite loop

name = ''
while True:
    print('What is your name?')
    name = input()
    if name == 'your name':
      break

    print('Thank you')