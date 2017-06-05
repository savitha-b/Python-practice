#dice rolling simulator

import random
import string
def dice_rolling():
    while True:
        roll = input('Roll the dice? Y/N: ')
        if roll == 'Y'|'y':
            dice = random.randint(1,6)
            print("number on the dice is: %d" %(dice))
        else:
            break

dice_rolling()
