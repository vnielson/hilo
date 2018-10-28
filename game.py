import random

print("Welcome to the HI - LO game")
number = random.randint(1, 100)
print("Guess a number between 1 & 100")

correctGuess = False

while not correctGuess:

    guess = int(input('Guess a number ... '))

    if guess == number:
        print('{} is the correct number, congratulations'.format(number))
        correctGuess = True
    elif guess < number:
        print(' {} is low'.format(guess))
    else:
        print('{} is high'.format(guess))
