'''
Script for calculating the geometric mean
Author: Felicia Fredlund
Last updated: 2025-02-10

How to run:
python(3) geometricmean.py

Examples:
python3 geometricmean.py
'''

def geomean(numbers):
    n = len(numbers)
    product = 1
    for number in numbers:
        product *= number
    return product ** (1/n)

def main():
    string_list = input("Calculate geometric mean with these numbers (put one space between numbers): ").split(" ")
    numbers = []
    for item in string_list:
        try:
            n = int(item)
            numbers.append(n)
        except ValueError:
            print("Not all values were numbers or you used punctuation, only one space between numbers.")
            return
    print(geomean(numbers))

main()