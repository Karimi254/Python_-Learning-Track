catName = []

while True:
    print('Enter name of the cat ' + str(len(catName) + 1) + '(or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catName = catName + [name]
    print('The cat names are:')
    for name in catName:
        print (' ' + name)
