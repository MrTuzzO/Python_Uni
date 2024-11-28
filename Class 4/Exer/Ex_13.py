import random

numToGuess = random.randint(1, 100)
guess = None
while guess != numToGuess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < numToGuess:
        print("Too low")
    elif guess > numToGuess:
        print("Too high")
print("Congratulations! You've guessed the correct number!")