'''
Script for take one file and replace a word with something else and save to a new file
Author: Felicia Fredlund
Last updated: 2025-01-22

Still to do:
1) add --o flag as optional parameter for overwriting file
2) add question with input if new file exists already, should it be overwritten?
https://docs.python.org/3/library/functions.html#input

How to run:
python(3) copyfilewithchanges.py FILENAME NEW-FILENAME WORD REPLACEMENT-WORD

Examples:
python3 copyfilewithchanges.py D0042D_Programmering/getfilecontent.txt D0042D_Programmering/newfile.txt Python C++
python copyfilewithchanges.py D0042D_Programmering/getfilecontent.txt D0042D_Programmering/newfile.txt Python Swedish
'''

import sys

def change(filename, new_filename, word, replacement_word):
    try:
        with open(filename) as f:
            content = f.read()
    except OSError as e:
        print("ERROR:", e)
        return
    
    replaced_content = content.replace(word, replacement_word)

    with open(new_filename, 'w') as f:
        f.write(replaced_content)

def main():
    if len(sys.argv) < 5:
        print("ERROR: Not enough parameters given. Four is needed in format: filename, new-filename, word, replacement-word")
        return
    
    change(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

main()