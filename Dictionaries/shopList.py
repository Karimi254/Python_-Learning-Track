#! /usr/bin/python3.6

"""A simple program to keep track of shopping items """

sList = {'Powder Soap': 'SunLight', 'Bathing Soap': 'Imperial Leather', 'Perfume': 'Black Shadow', 'Lotion': 'Nivea for Men', 'Tooth Paste': 'Colgate natural extract', 'Toothbrush': 1}

while True:
    print('Enter the item name (Blank to exit)' )

    item = input()
    
    if item == '':
        break

    if item in sList:
        print(sList[item] + ' is available for use from ' + item)
       
    else:
        print('Details for ' + item + ' not available in the shopping basket')
        print('What is the item brand ?')
        brand = input()
        sList[item] = brand
        print('Shopping List basket database updated')
