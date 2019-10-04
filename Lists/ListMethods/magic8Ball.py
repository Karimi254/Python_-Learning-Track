import random
try:

    messages = ['Hi',
    'You think',
    'you know me?',
    'No you dont',
    ' i am nick',
    # 'a dangerous',
    'python programmer',
    'i can automate',
    'your life.']

    print(messages[random.randint(0, len(messages) -1)])
except IndentationError:
    print('Error: unexpected indent')
