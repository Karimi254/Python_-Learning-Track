def spam():
    global egg
    egg = "I am global"
    bacon()
def bacon():
    egg = 'Hello, egg'
spam()
print(egg)
