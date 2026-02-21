'''⛮POWERED BY||SALEH AMOO|| GUESS GAME Δ'''
#┄┄┄┅┅❅✾❅┅┅┄┄┄
import random
print("Welcome to the guess game.DELTAΔ")
max = int(input("Enter the range of game."))
secretNumber = random.randint(1, max)
print('I am thinking of a number between 1 and %d.' %max )
# Ask the player to guess 6 times.
for guessesTaken in range(1, 87):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))