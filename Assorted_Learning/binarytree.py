#!/usr/bin/env python3

'''
Script for the binary search tree data structure that holds integers as value.
An AVL tree so a balanced tree have max 1 difference in height between the right and left side.

Author: Felicia Fredlund

Last updated: 2025-XX-XX
'''


# THE UNIT TESTS SHOULD TEST THE BEHAVIOR, NOT THE IMPLEMENTATION DETAILS
# Test the API of my software. So anything anyone outside using it would touch.
# What are the requirements of my BST? Those are the things I should test.
# Searching should give me the node (or min/max) that I'm looking for.
# The requirements of a node is to get value and children.
# I can use the setUp(self) method to set up a BST, don't forget
# if __name__ == "__main__":
#    unittest.main()


from __future__ import annotations
# Above is so I can have type hinting in methods inside the class referring to the class

class _Node:
    def __init__(self, value: int):
        '''TEXT'''
        # __value, __left_child, __right_child
        pass

    def __repr__(self) -> str:
        return f"_Node({self.getValue()})"

    def getValue(self) -> int:
        '''TEXT'''
        pass

    def getLeftChild(self) -> _Node:
        '''TEXT'''
        pass

    def getRightChild(self) -> _Node:
        '''TEXT'''
        pass

    def setLeftChild(self, node: _Node) -> _Node:
        '''TEXT'''
        pass

    def setRightChild(self, node: _Node) -> _Node:
        '''TEXT'''
        pass

class Tree:
    def __init__(self):
        self.__root = None

    def __str__(self) -> str:
        '''TEXT'''
        # Call one of preorder/postorder/inorder
        pass

    def __repr__(self) -> str:
        '''TEXT'''
        pass

    def getRoot(self) -> int:
        '''TEXT'''
        pass

    def getHeight(self) -> int:
        '''TEXT'''
        # call _getHeight()
        pass

    def getMin(self) -> int:
        '''TEXT'''
        pass

    def getMax(self) -> int:
        '''TEXT'''
        pass

    def search(self, value: int, use_bfs_over_dfs: bool = False) -> int:
        '''TEXT'''
        # if use_bfs_over_dfs is False, use dfs; if true, use bfs
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

    def insert(self, value: int):
        '''TEXT'''
        # call _balance() when implemented
        pass

    def delete(self, value: int):
        '''TEXT'''
        # call _balance() when implemented
        pass


    # Private methods

    def _getHeight(self, root: _Node = None) -> int:
        '''TEXT'''
        # if root is None, work with self.__root
        pass

    def _isBalanced(self) -> bool:
        '''TEXT'''
        # Use __getHeight on left and right child of root to learn if they are balanced
        pass

    def _balance(self, value):
        '''TEXT'''
        # call __isBalanced() to figure out if it needs balancing
        pass