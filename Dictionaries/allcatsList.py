#Using lists

catNames = []

while True:
    print('Enter catName' + str(len(catNames) +1) + '(Or blank to exit)')
    name = input()

   #Check if name blank

    if name == '':

        break

    catNames = catNames + [name]

    print('The cat names are: ')

    for names in catNames:

        print(' ' + name)
