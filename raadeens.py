import os
import random
import time

def clear():
    command = 'cls'
    os.system(command)
clear()
print('You have to guess a number. It ranges from 1 to 1000. You will have 10 tries per round, there are 20 rounds.')
print('If you guess the number right, you\'ll get a point, if not, it will move on to the next round')
#time.sleep(6)
random_nr = random.randint(1, 1000)
g1 = input('Round 1, guess: ')
while g1 != random_nr: 
    if g1 == random_nr:
        print('You got it!')
