def someFunc(addItem):
    addItem.insert(3, 'and')
spam = ['apples', 'banana', 'tofu', 'cat']
someFunc(spam)
print(spam)
