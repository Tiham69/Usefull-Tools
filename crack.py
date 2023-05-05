from string import digits, ascii_letters, punctuation, ascii_lowercase
from itertools import product

for i in range(26):
    for passcode in product(ascii_lowercase, repeat=i): # can be used that was imported form string = ascii_lowercase, digits, punctuation, ascii_letters and many more
            print(*passcode)

# This code can be useful to crack a phones password