'''
Script for given an integer, print all numbers from there to zero and then back up to that number with recursion
Author: Felicia Fredlund
Last updated: 2025-01-XX

Still to do: n/a

How to run:
python(3) lab2-bounce.py NUMBER_OF_BOUNCES

Examples:
python3 lab2-bounce.py 3
python lab2-bounce.py 12


bounce(4)
4 3 2 1 0 1 2 3 4
bounce(7)
7 6 5 4 3 2 1 0 1 2 3 4 5 6 7
bounce(0)
0
'''
import sys


def bounce(n):
    pass

def main():
    if len(sys.argv) < 2:
        print("ERROR: Number of bounces not given.")
    pass

main()