'''
Script for take one file and replace a word with something else and save to a new file
Author: Felicia Fredlund
Last updated: 2025-01-22

Still to do: n/a

How to run:
python(3) lab2-replaceword.py FILENAME NEW-FILENAME WORD REPLACEMENT-WORD

Examples:
python3 lab2-replaceword.py getfilecontent.txt newfile.txt Python C++
python lab2-replaceword.py getfilecontent.txt newfile.txt Python C++
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