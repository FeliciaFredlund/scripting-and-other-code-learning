'''
Script for a function that takes a list and divides it into two, by putting every other item in the second list.
Author: Felicia Fredlund
Last updated: 2025-02-10

How to run:
python(3) everyother.py

Examples:
python3 everyother.py
'''

def everyother(lst):
    return lst[::2], lst[1::2] 

def main():
    lst = input("Write a list of elements with spaces between each element: ").split(" ")
    print (everyother(lst))

main()