#!/usr/bin/env python3

'''
Script for writing insert sort from scratch as practice
Author: Felicia Fredlund
Last updated: 2025-05-19

How to run:
python(3) insertsort.py PARAMETERS

Examples:
python3 Assorted_Learning/insertsort.py
EXAMPLE
'''

''' FOR LATER: MIGHT WANT TO PUT IT IN ITS OWN SCRIPT OR JUST COPY IT OVER - maybe make a small CLI to test sorting algos
import sys

if len(sys.argv) != 1:
    # Save the parameters as the list to be sorted
    pass
else:
    # Start interaction to get a list
    pass
'''

def main():
    nums = [4, 5, 3, 2, 0, 1, 6, 9, 8, 7] # [2, 3, 5, 1, 4] # [8, 2, 8, 1, 3, 9, 5] # 
    sorted_nums = insert_sort(nums.copy())
    expected = sorted(nums)
    
    print(f"\nOriginal list: {nums}\n")
    print(f"Expected result: {expected}\n")
    print(f"Result: {sorted_nums}\n")
    print(f"Is expected result and result the same? {expected == sorted_nums}\n")

def insert_sort(data):
    if len(data) < 2:
        return data
    
    i = 1
    while i < len(data):
        j = i
        
        while j > 0:
            if data[j] < data[j-1]:
                temp = data[j]
                data[j] = data[j-1]
                data[j-1] = temp
            j -= 1

        i += 1

    return data


main()

'''
Here is boot.dev's solution to insert sort:

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

I missed big here. My list will go through all indexes to the left even after it knows all is sorted.
Boot.dev's code on the other hand does not.
It also showed how to switch the variables without temp, which I had forgotten.
So short and smooth.

AND NO BASE CASE IS NECESSARY. Sadge.

'''