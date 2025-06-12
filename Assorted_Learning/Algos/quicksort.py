#!/usr/bin/env python3

'''
Script for writing quick sort from scratch as practice
Author: Felicia Fredlund
Last updated: 2025-05-20

How to run:
python(3) quicksort.py PARAMETERS

Examples:
python3 Assorted_Learning/quicksort.py
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
    nums = [8, 3, 2, 9, 1, 7, 6, 10, 4, 5] # [4, 5, 3, 2, 0, 1, 6, 9, 8, 7] # [8, 2, 8, 1, 3, 9, 5] #
    sorted_nums = nums.copy()
    quick_sort(sorted_nums, 0, len(nums) - 1)
    expected = sorted(nums)
    
    print(f"\nOriginal list: {nums}\n")
    print(f"Expected result: {expected}\n")
    print(f"Result: {sorted_nums}\n")
    print(f"Is expected result and result the same? {expected == sorted_nums}\n")

def quick_sort(data, low, high):
    if low < 0 or high >= len(data) or high-low < 1:
        return
    
    first_pivot = partition(data, low, high)

    quick_sort(data, low, first_pivot-1)
    quick_sort(data, first_pivot+1, high)

def partition(data, low, high):
    pivot = high
    i = low - 1
    j = low
    while j < high:
        if data[j] < data[pivot]:
            i += 1
            data[i], data[j] = data[j], data[i]
        j += 1
    data[i+1], data[pivot] = data[pivot], data[i+1]
    
    return i+1


main()

'''
Here is boot.dev's solution to insert sort:

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

As ALWAYS, better base case.
Although I guess I have some basic error handling if sending in weird low and high in the first call.
Using FOR loop instead of WHILE when going through a range, once again, silly me.
I also liked how they saved pivot as nums[high], so it just holds the value.
Also, could totally skip that in my solution and just use data[high]. Less clear it is the pivot, but...

'''