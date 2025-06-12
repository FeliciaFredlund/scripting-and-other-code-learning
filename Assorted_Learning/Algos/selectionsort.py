#!/usr/bin/env python3

'''
Script for writing selection sort from scratch as practice
Author: Felicia Fredlund
Last updated: 2025-05-20

How to run:
python(3) selectionsort.py PARAMETERS

Examples:
python3 Assorted_Learning/selectionsort.py
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
    sorted_nums = selection_sort(nums.copy())
    expected = sorted(nums)
    
    print(f"\nOriginal list: {nums}\n")
    print(f"Expected result: {expected}\n")
    print(f"Result: {sorted_nums}\n")
    print(f"Is expected result and result the same? {expected == sorted_nums}\n")

def selection_sort(data):
    for low_index in range(len(data)):
        lowest = low_index
        for i in range(low_index, len(data)):
            if data[i] < data[lowest]:
                lowest = i
        
        data[low_index], data[lowest] = data[lowest], data[low_index]

    return data


main()

'''
Here is boot.dev's solution to insert sort:

def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums

I missed that the inner for loop could start its range at low_index + 1 since I compared with lowest.

'''