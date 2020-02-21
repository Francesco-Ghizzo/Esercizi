#count the number of occurrencies of a letter in a string using dictionaries

import sys

def get_string():

    string = raw_input()
    if string == '':
        sys.exit()
    else:
        return string



def letter_count(text):

    count = {}
    for char in text:
        count.setdefault(char, 0)
        count[char] = count[char] + 1
    return count


while True:
    keyboard_input = get_string()
    print(letter_count(keyboard_input))
