from string import digits, ascii_letters, punctuation, ascii_lowercase
from itertools import product

for passcode in product(digits, repeat=4): # can be used that was imported form string = ascii_lowercase, digits, punctuation, ascii_letters and many more
        print(*passcode)

# This code can be useful to crack a phones password