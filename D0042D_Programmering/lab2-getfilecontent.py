'''
Script for prints the contents of the given file
Author: Felicia Fredlund
Last updated: 2025-01-22

How to run:
python(3) lab2-getfilecontent.py FILENAME

Examples:
python3 lab2-getfilecontent.py FILENAME
python lab2-getfilecontent.py FILENAME
'''
import sys

def get_file_content(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except OSError as e:
        print(f"ERROR: {e}.")
        return

    print(content)

def main():
    if len(sys.argv) < 2:
        print("ERROR: No file name given.")
        return
    
    get_file_content(sys.argv[1])

main()