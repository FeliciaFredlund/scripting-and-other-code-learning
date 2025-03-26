#!/usr/bin/env python3

'''
Script for take one file and replace a word with something else and save to a new file
Author: Felicia Fredlund
Last updated: 2025-02-03

How to run:
python(3) copyfilewithchanges.py FILENAME NEW-FILENAME WORD REPLACEMENT-WORD (--o)
# --o is an optional flag. If sent then the new file will be overwritten if it exists
# If --o isn't sent and the new file exists, the user will be asked if they want to overwrite or not

Examples:
python3 Scripts/copyfilewithchanges.py D0042D_Programmering/getfilecontent.txt D0042D_Programmering/newfile.txt Python C++
python D0042D_Programmering/copyfilewithchanges.py D0042D_Programmering/getfilecontent.txt D0042D_Programmering/newfile.txt Python Swedish
'''

import sys

def change(filename, new_filename, word, replacement_word, flag=""):
    try:
        with open(filename) as f:
            content = f.read()
    except OSError as e:
        print("ERROR:", e)
        return
    
    replaced_content = content.replace(word, replacement_word)

    try:
        with open(new_filename) as f:
            if flag == "--o":
                pass
            else:
                while True:
                    answer = input("The new file already exists. Do you want to overwrite it? (y/n) ")
                    if len(answer) != 0:
                        if answer.lower()[0] == "y":
                            break
                        if answer.lower()[0] == "n":
                            print("Operation aborted as chosen by user.")
                            return
                    print("Please answer with y or n.")
    except OSError as e:
        pass

    with open(new_filename, 'w') as f:
        f.write(replaced_content)
    print(f"{new_filename} is now filled with the content of {filename} with {word} replaced by {replacement_word}.")

def main():
    if len(sys.argv) < 5:
        print("ERROR: Not enough parameters given. Four is needed in format: filename, new-filename, word, replacement-word")
        return
    
    change(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "")

main()