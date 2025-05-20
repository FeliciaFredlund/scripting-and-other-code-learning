#!/usr/bin/env python3

'''
Script for writing merge sort from scratch as practice
Author: Felicia Fredlund
Last updated: 2025-05-19

How to run:
python(3) mergesort.py PARAMETERS

Examples:
python3 Assorted_Learning/mergesort.py
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
    sorted_nums = merge_sort(nums.copy())
    expected = sorted(nums)
    
    print(f"\nOriginal list: {nums}\n")
    print(f"Expected result: {expected}\n")
    print(f"Result: {sorted_nums}\n")
    print(f"Is expected result and result the same? {expected == sorted_nums}\n")


# I missed the data case of an empty list. Could have just added if len(data) == 0: return []
# That was my first thought. Boot.dev suggested:
# if len(data) < 2:
#     return data
# The benefit of this is you case the 0 len list as well as the smallest list for the general function too.

def merge_sort(data):
    if len(data) == 1:
        return data
    
    mid = len(data) // 2
    return merge(merge_sort(data[:mid]), merge_sort(data[mid:]))

def merge(first, second):
    sorted = []
    f_index = 0
    s_index = 0
    
    while f_index < len(first):
        if first[f_index] <= second[s_index]:
            sorted.append(first[f_index])
            f_index += 1
        else:
            sorted.append(second[s_index])
            s_index += 1
        
        if len(second) == s_index:
            sorted += first[f_index:]
            break
    sorted += second[s_index:]
    
    return sorted


main()

'''
Here is boot.dev's solution to merge sort:

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[: len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final

My take away from looking at both of them.
Mine does use a bit more memory since I splice the list again at the end of merge.
Might be better to just do the while loops as they do.
I also missed the much better base case plus catching an empty list
'''