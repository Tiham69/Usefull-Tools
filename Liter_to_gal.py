import os
import sys
import random

def main():

    try: # checks if only number is inputed or not
        a = int(input('Enter the range of gallon-chart: '))


        print('Gallon     Liter')

        for i in range(1, a+1):
            li = i * 3.785 # gal to liter convert

            if i <= 9: # for esthetic
                print(f'{i:0.1f}        {li:.2f}') # formating in py f'{(4/3):10.2f}' | f'{a:.2f}'
            else:
                print(f'{i:.1f}       {li:.2f}')

    except ValueError:
        print('Enter a number.')

if __name__ == '__main__':
    main()