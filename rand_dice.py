#random dice number generator

import sys, random

def dice():
    print(random.randint(1, 6))

while True:
    input = raw_input()
    if input == 'exit':
        sys.exit()
    else:
        dice()
