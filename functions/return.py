import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It was decidedly so"
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again.'
    elif answerNumber == 5:
        return "Ask agin later"
    elif answerNumber == 6:
        return 'Yak shaving'
    elif answerNumber == 7:
        return 'Incredibly boring.'
    elif answerNumber == 8:
        return 'Oh whats with programmers'
    elif answerNumber == 9:
        return 'Dangerous'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
