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
    # each time this is called it prints n twice
    # between those print statements is the recursive call
    # base case is n=0 when n is printed only once and then ended with return
    # please add a print() statement after the call of this function to end the line

    print(n, end=' ')

    if n == 0:
        return
    else:
        bounce(n-1)

    print(n, end=' ')

def main():
    if len(sys.argv) < 2:
        print("ERROR: Number of bounces not given.")
        return
    
    try:
        number_of_bounces = int(sys.argv[1])
    except ValueError:
        print(f"ERROR: The parameter, {sys.argv[1]}, is not an integer.")
        return
    
    bounce(number_of_bounces)
    print()

main()