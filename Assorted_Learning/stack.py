#!/usr/bin/env python3

'''
Script for implementing a stack data structure from the ground up
Author: Felicia Fredlund
Last updated: 2025-05-21
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(self.size(), item)

    def pop(self):
        last_index = self.size() - 1
        if (last_index < 0):
            return None
        item = self.items[last_index]
        del self.items[last_index]
        return item

    def peek(self):
        size = self.size()
        return self.items[size - 1] if size > 0 else None

    def size(self):
        # using len(self.items) might actually be okay since it is a Python function, not a list function... Hmmm...
        i = 0
        while True:
            try:
                self.items[i]
                i += 1
            except IndexError:
                break
        return i