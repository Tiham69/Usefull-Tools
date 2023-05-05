import sys
import os
import random

def main(): # main function for python

    lim = 1 # subject count
    sub = 0 # marks sumer initializator
    a = 0   # mark's input taker init
    print('Enter 8 subject mark\'s: ')

    while lim != 9:

        try:# see's if there is user typed in number or not
            a = int(input(f'Subject Number {lim}: '))
        except ValueError:
            print('Enter Number\'s')
            continue

        # checks if any subjects is failed
        if a < 33 and a >= 0:
            print('You Failed!!')
            break
        # checks if marks are in 0 to 100
        if a > 100 or a < 0:
            print('Mark\'s are between 0-100 ')
            print(sub)
            continue

        # subject count
        lim += 1
        # to avoid errors
        b = a
        # total marks sumer
        sub += b

    if sub >= 0 and sub <= 1200: # error avoiding
        if sub >= 600:
            print(f'Passed in First Division. Mark\'s = {sub}')
        elif sub >= 450 and sub < 600:
            print(f'Passed in Second Division. Mark\'s  = {sub}')
        elif sub >= 330 and sub < 450:
            print(f'Passed in Third Division. Mark\'s = {sub}')
        elif sub < 330:
            print(f'You Failed!!. BTW Mark\'s = {sub}')
    else:
        print('You entered wrong mark\'s')

if __name__ == '__main__':
    main()