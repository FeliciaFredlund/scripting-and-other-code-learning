#!/usr/bin/env python3

'''
Script for writing bubble sort from scratch as practice
Author: Felicia Fredlund
Last updated: 2025-05-19

How to run:
python(3) bubblesort.py PARAMETERS

Examples:
python3 Assorted_Learning/bubblesort.py
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
    nums = [8, 2, 8, 1, 3, 9, 5]
    sorted_nums = bubble_sort(nums.copy())
    expected = sorted(nums)
    
    print(f"\nOriginal list: {nums}\n")
    print(f"Expected result: {expected}\n")
    print(f"Result: {sorted_nums}\n")
    print(f"Is expected result and result the same? {expected == sorted_nums}\n")


def bubble_sort(data):
    end_index = len(data) - 1
    cycles = 0
    
    while end_index > 0:
        stopped_swapping_early = -1

        for i in range(0, end_index):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                stopped_swapping_early = -1
            elif stopped_swapping_early == -1:
                stopped_swapping_early = i

        end_index = end_index - 1 if stopped_swapping_early == -1 else stopped_swapping_early 
        cycles += 1  
    
    print(f"{cycles=}")
    return data

main()

'''
Here is boot.dev's solution to bubble sort:

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums

Their solution to use swapping is better than my end_index.
I didn't think of putting swapping to false as the first step,
which is why my first implementation with swapping didn't work.
That they decided to use end as length of list to start and go from range(1, end) is just a different way of doing it.

So my biggest problem was how to handle the bigger loop, and doing that efficiently. The sorting I had a fine grip on.

Boot.dev doesn't show it hear, but later shows that the temp variable isn't needed.
nums[i], nums[i-1] = nums[i-1], nums[i]
'''