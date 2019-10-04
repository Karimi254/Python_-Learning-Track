# A program that lets the user type a Programming book and checks whethers its in the list

p_books = ['Python the Hard Way', 'Python Cookbook', 'Java', 'C', 'PHP']
print ('Type a book name: ')
name = input()
if name not in p_books:
    print('Sorry, we dont have ' + name + ' programming book in store.')
else:
    print(name + ' book found.')
