'''
Script for testing ord and chr methods in Python
Author: Felicia Fredlund
Last updated: 2025-02-10

Still to do:
### ord()
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

### chr()
Return the string representing a character whose Unicode code point is the integer i.
For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16).
ValueError will be raised if i is outside that range.

How to run:
python(3) FILENAME.py PARAMETERS

Examples:
EXAMPLE
EXAMPLE
'''
import string

def rotate_word(phrase, rotation):
    words = phrase.split(" ")
    coded_phrase = ""
    for word in words:
        for char in word:
            if char not in string.punctuation:
                coded_phrase += chr(ord(char)+rotation)
            else:
                coded_phrase += char
        coded_phrase += " "
    return coded_phrase.rstrip()

def main():
    print("This follows the ascii table, btw.")
    phrase = input("Please write the word/phrase you want to encrypt: ")
    rotation = 0
    while True:
        rotation = input("How much do you want to rotate it: ")
        try:
            rotation = int(rotation)
            break
        except:
            print("That is not a number. Please add a number.")

    coded_phrase = rotate_word(phrase, rotation)

    print("Your coded phrase is:", coded_phrase)

main()