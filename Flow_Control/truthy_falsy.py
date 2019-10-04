#Truth and False Values('', 0, 0.0)

name = ''
while not name: #!= name
    print('What is your name')
    name = input()
print('how many guests do you expect?')
numOfguest = int(input())
if numOfguest: #!=0
    print("Be sure to book enough rooms for your guests.")
print('Done')
