# importing the time module

import time

# welcoming the user
name = raw_input('what is your name?')
print('Hello,' + name, "Time to play hangman!")
print('')

# wait for 1 second
time.sleep()

print()
'start guessing...'
time.sleep(0.5)

# here we set the secret
word = 'secret'

# creates an variable with an empty value
guesses = ''