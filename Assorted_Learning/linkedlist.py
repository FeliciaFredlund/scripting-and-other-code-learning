#!/usr/bin/env python3

'''
Script for implementing the linked list data structure.
Author: Felicia Fredlund
Last updated: 2025-XX-XX
'''

from __future__ import annotations
# Above is so I can have type hinting in methods inside the class referring to the class

class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__previous = None

    def __repr__(self):
        '''What prints if using print on it'''
        return str(self.__value)

    def set_next(self, node: Node):
        '''Set the next node property'''
        self.__next = node

    def set_previous(self, node: Node):
        '''Set the previous node property'''
        self.__previous = node

    def set_value(self, value):
        '''Set the value property'''
        self.__value = value

    def get_next(self) -> Node:
        '''Get get the next node'''
        return self.__next
    
    def get_previous(self) -> Node:
        '''Get the previous node'''
        return self.__previous
    
    def get_value(self) -> Node:
        '''Get the value of the node'''
        return self.__value
    
class LinkedList:
    def __init__(self):
        '''Creates an empty LinkedList'''
        self.__size = 0
        self.__head = None
        self.__tail = None

    def __iter__(self):
        '''Returns an iterator'''
        current_node = self.__head
        while current_node is not None:
            yield current_node
            current_node = current_node.get_next()

    def __repr__(self):
        print = "LinkedList < "
        for node in self:
            print += str(node.get_value()) + " "
        print += ">"
        return print

    def is_empty(self) -> bool:
        '''Check if the linked list is empty'''
        return self.__size == 0

    def size(self) -> int:
        '''Get size of linked list'''
        return self.__size

    def get_head(self) -> Node:
        '''Get first node'''
        return self.__head

    def get_tail(self) -> Node:
        '''Get last node'''
        return self.__tail

    def get(self, index: int) -> Node:
        '''Get node at index'''
        if index < 0 or index >= self.size():
            return None
        
        i = 0
        current_node = None
        for node in self:
            current_node = node
            if i == index:
                break
            i += 1
        
        return current_node


    ## Appending/Inserting
    def append(self, new_node: Node):
        '''Append to the end. Will be last node of the linked list'''
        if self.is_empty():
            self.__head = new_node
            self.__size = 1
            return
        
        if self.__tail is None: # aka the list has only one element (__head)
            self.__head.set_next(new_node)
            self.__tail = new_node
            self.__tail.set_previous = self.__head
            self.__size = 2
            return
        
        self.__tail.set_next(new_node)
        new_node.set_previous(self.__tail)
        new_node.set_next(None)
        self.__tail = new_node
        self.__size += 1
    
    def prepend(self, new_node: Node):
        '''Append to the front/start of the linked list'''
        pass

    def insert_after(self, insertion_point: Node, new_node: Node):
        '''Insert after a certain node'''
        pass

    def insert_before(self, insertion_point: Node, new_node: Node):
        '''Insert before a certain node'''
        pass

    def insert_at_index(self, index: int, new_node: Node):
        '''Insert the new node at index'''
        pass

    def extend(self, new_node: Node):
        '''Extends the link list with multiple Nodes already linked through the next property'''
        pass

    def preextend(self, new_node: Node):
        '''Extends the front of the link list with multiple Nodes already linked through the next property'''
        pass

    # Removing/deleting
    def remove_tail(self) -> Node: 
        '''Remove the last node and return it'''
        pass

    def remove_head(self) -> Node:
        '''Remove the first node and return it'''
        pass

    def remove(self, node_to_remove: Node):
        '''Remove a specific node'''
        pass

    def remove_at_index(self, node_to_remove: Node):
        '''Remove the node at index'''
        pass