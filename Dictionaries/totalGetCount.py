allGuest = {'Nicholas': {'apples': 10, 'banana': 6},
            'Esther': {'oranges': 4, 'apples':4},
            'Frank': {'sandwich': 4, 'oranges': 8}}
def totalBrought(guest, item):
    numBrought = 0
    for k, v in guest.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print('- Apples     ' + str(totalBrought(allGuest, 'apples')))
print('- Oranges     ' + str(totalBrought(allGuest, 'oranges')))
print('- Bananas     ' + str(totalBrought(allGuest, 'banana')))
print('- Sandwich     ' + str(totalBrought(allGuest, 'sandwich')))
