#! /usr/bin/python3.6

#This program stores date of my best friends birthday

birthdays = {'Dennis': 'Dec 8', 'Marie': 'Dec 13', 'Purity':'Mar 4' }

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I dont have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
