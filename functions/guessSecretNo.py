# This is a guess number game
import random

secretNumber = random.randint(1, 20)
print('I\'m thinking of a number between 1 and 20. ')

# Ask player guess 6 times
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess was too low.')
    elif guess > secretNumber:
        print('Your guess was too high.')
    else:
        break
# The correct guess
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses.')
else:
    print("Nope. The number i was thinking was, " + str(secretNumber))
