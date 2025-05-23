#!/usr/bin/env python3

'''
Script for implementing the linked list data structure.
Author: Felicia Fredlund
Last updated: 2025-XX-XX
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
    
class LinkedList:
    def __init__(self):
        pass