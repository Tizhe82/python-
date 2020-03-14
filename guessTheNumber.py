# This is a guess the number game.

import random # imports random module so that it can use the random.randint() for the user to guess
SecretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1,7): #the program tells the player that it has come up with a secret number and it will give the player six chances to guess it.
    print('Take a guess.')
    guess = int(input())

    if guess < SecretNumber:
        print('Your guess is too low.')
    elif guess > SecretNumber:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!
if guess == SecretNumber:
  print('Good job! You guessed my number in' + str(guessTaken) + 'guesses!')
else:9
    print('Nope. The number I was thinking of was' + str(SecretNumber))