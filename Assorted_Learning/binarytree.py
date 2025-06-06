#!/usr/bin/env python3

'''
Script for datastructure: binary search tree.
Author: Felicia Fredlund
Last updated: 2025-XX-XX
'''

from __future__ import annotations
# Above is so I can have type hinting in methods inside the class referring to the class

class Node:
    def __init__(self, value: int):
        '''TEXT'''
        # value, left_child, right_child
        pass

    def __str__(self) -> str:
        '''TEXT'''
        pass

    def __repr__(self) -> str:
        '''TEXT'''
        pass

    def getValue(self) -> int:
        '''TEXT'''
        pass

    def getLeftChild(self) -> Node:
        '''TEXT'''
        pass

    def getRightChild(self) -> Node:
        '''TEXT'''
        pass

class Tree:
    def __init__(self):
        '''TEXT'''
        self.__root = None

    def __str__(self) -> str:
        '''TEXT'''
        pass

    def __repr__(self) -> str:
        '''TEXT'''
        pass

    def getRoot(self) -> Node:
        '''TEXT'''
        pass

    def getHeight(self) -> int:
        '''TEXT'''
        pass

    def getMin(self) -> Node:
        '''TEXT'''
        pass

    def getMax(self) -> Node:
        '''TEXT'''
        pass

    def search(self, value) -> Node:
        '''TEXT'''
        pass


    # Representation of tree

    def preorder(self, visited) -> list[int]:
        '''TEXT''' # Took the visited param from boot.dev, will see if this is how I do it
        pass

    def postorder(self, visited) -> list[int]:
        '''TEXT''' # Took the visited param from boot.dev, will see if this is how I do it
        pass

    def inorder(self, visited) -> list[int]:
        '''TEXT''' # Took the visited param from boot.dev, will see if this is how I do it
        pass


    # Insert/Delete

    def insert(self, value):
        '''TEXT'''
        pass

    def delete(self, value):
        '''TEXT'''
        pass


    # Balancing an unbalanced tree

    def isBalanced(self) -> bool:
        '''TEXT'''
        pass

    def balance(self, value):
        '''TEXT'''
        pass

    
    # Self balancing version

    def insertSelfBalancing(self, value):
        '''TEXT'''
        pass

    def deleteSelfBalancing(self, value):
        '''TEXT'''
        pass