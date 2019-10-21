guess = input ('Pick a number between 1 and 10:')
guess = int(guess)
import random
surprise = random.randint(1,10)
if guess == surprise:
    print('True')
else:
    print ('Try again')
    guess = input()
    guess = int(guess)
    if guess == surprise:
        print ('True')
    else: 
        print ('Try again')
        guess = input()
        guess = int(guess)
        if guess == surprise:
         print ('True')
        else:
            print ('No Luck')
            

