ages = [12, 43, 45, 9,24, 89]
ages.sort(reverse=True)
print(ages)

try:

    animals = ['duck', 'cow', 23, 89, 'rat']
    animals.sort()
    print(animals)
except TypeError:
    print('Error: Python cant sort int and string together.')

# sort alphabetically
alpha = ['a', 'z', 'A', 'Z']
alpha.sort(key=str.lower)
print(alpha)
