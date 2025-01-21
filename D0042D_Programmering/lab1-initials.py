'''
Script for printing initials to terminal/idle
Author: Felicia Fredlund
Last updated: 2025-01-21

Still to do: Add the rest of the alphabet (abcdeijklmnrsuvwxyzåäö)

How to run:
python(3) lab1-initials.py INITIALS

Examples:
python3 lab1-initials.py Ff
python3 lab1-initials.py gT
python lab1-initials.py POH
'''

import sys

# Prints each initial after each other
def print_initials():
    if (len(sys.argv) < 2):
        print("ERROR: No parameter (initials) given.")
        return

    initials = sys.argv[1]

    if (not initials.isalpha()):
        print("ERROR: Initials are letters only. Ex: EG, eG, Eg, eg.")
        return
    
    initials = initials.lower()

    lines = ["", "", "", "", "", "", ""]

    for letter in initials:
        letter_list = letter_asterisk_list(letter)
        line_index = 0
        for line in letter_list:
            for position_index in range(0,7):
                if position_index in line:
                    lines[line_index] += "*"
                else:
                    lines[line_index] += " "
            lines[line_index] += "   "
            line_index += 1

    for line in lines:
        print(line)


# Finds the right list of list with index for asteriks
def letter_asterisk_list(letter):
    match letter:
        case "f":
            return [[0, 1, 2, 3, 4, 5, 6], [0], [0, 1, 2, 3], [0], [0], [0]]
        case "g":
            return [[2, 3, 4], [1, 5], [0], [0, 4, 5, 6], [1, 5], [2, 3, 4]]
        case "h":
            return [[0, 6], [0, 6], [0, 1, 2, 3, 4, 5, 6], [0, 6], [0, 6], [0, 6]]
        case "o":
            return [[2, 3, 4], [1, 5], [0, 6], [0, 6], [1, 5], [2, 3, 4]]
        case "p":
            return [[0, 1, 2, 3, 4], [0, 5], [0, 5], [0, 1, 2, 3, 4], [0], [0]]
        case "q":
            return [[2, 3, 4], [1, 5], [0, 6], [0, 6], [1, 5], [2, 3, 4, 6]]
        case "t":
            return [[0, 1, 2, 3, 4, 5, 6], [3], [3], [3], [3], [3]]
        case _:
            return [[], [], [], [], [], []]
        

print_initials()