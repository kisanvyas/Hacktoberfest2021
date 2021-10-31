#!/usr/bin/env python3
import random
import sys

print('\n\t\tHi there! Welcome to dice rolling simulator.\n')
inp = 1
uinp = 'yes'

while (inp):
    if inp == 1:
        dice = random.randint(1,6)
        print('\t\t\tDice says: ', dice, '\n')
        uinp = input('\t\tDo you wanna roll again? ')
    else:
        uinp = input("\t\tPrint 'yes' or 'no'\n Wanna roll the dice once more? ")
    if uinp.lower() == 'yes' or uinp.lower() == 'y':
        inp = 1
    elif uinp.lower() == 'no' or uinp.lower() == 'n':
        inp = 0
    else:
        inp = 2

print("\nGood bye!\n")
