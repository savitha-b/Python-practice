#dice rolling simulator

import random
import string
def dice_rolling():
    i = True
    while i is True:
        print 'You have rolled: ', random.randint(1,6)
        roll = raw_input('Roll the dice? (Y) / (N) : ')
    if roll == ('Y' or 'y'):
        i = True
    else:
        i = False

dice_rolling()
