guess = input ('Pick a number between 1 and 10:')
guess = int(guess)
import random
surprise = random.randint(1,10)
print ('The answer is' +str(surprise))
print(bool(guess == surprise))
