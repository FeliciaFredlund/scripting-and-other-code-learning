#!/usr/bin/env python3

'''
Script for implementing the queue data structure.
Author: Felicia Fredlund
Last updated: 2025-05-23

'''

class Queue:
    def __init__(self):
        self.items = []
        self.__size = 0

    def enqueue(self, item):
        self.items.insert(0, item)
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            return None
        item = self.items[self.__size - 1]
        del self.items[self.__size - 1]
        self.__size -= 1
        return item

    def peek(self):
        if self.__size == 0:
            return None
        return self.items[self.__size - 1]

    def size(self):
        return self.__size