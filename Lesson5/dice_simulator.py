#dice rolling simulator

import random
import string
def dice_rolling():
    dice = random.randint(1,6)
    ans = raw_input('Roll the dice? (Y) / (N) : ')
        roll = input('Roll the dice? Y/N: ')
    while ans == 'Y':
        print "number on the dice is: %d" %(dice)
    else:
        break

dice_rolling()
