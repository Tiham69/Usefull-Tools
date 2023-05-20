import sys
import os
import random

def main():

    n = int(input('Enter a number: '))

    print(f'{s_fact(n)}')

def s_fact(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

if __name__ == '__main__':
    main()