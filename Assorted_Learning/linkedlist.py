#!/usr/bin/env python3

'''
Script for implementing the linked list data structure.
Author: Felicia Fredlund
Last updated: 2025-06-05
'''

from __future__ import annotations
# Above is so I can have type hinting in methods inside the class referring to the class

class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__previous = None

    def __str__(self):
        '''The string version of a Node'''
        return str(self.__value)
    
    def __repr__(self):
        '''The string representation of coding a Node'''
        return f"Node({self.__value})"
    
    def __eq__(self, other):
        '''Test if the __value of two nodes are the same or if node.__value is same as the value sent in'''
        if isinstance(other, Node):
            return self.__value == other.__value
        return self.__value == other

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

    def __str__(self):
        '''String representation of a LinkedList, as LinkedList < Node Node Node >'''
        string = "LinkedList < "
        for node in self:
            string += str(node) + " "
        string += ">"
        return string

    def __repr__(self):
        '''Code representation of how a LinkedList could be created. Don't call on large lists.'''
        code = "LinkedList()"
        for node in self:
            code += ".append(" + repr(node) + ")"
        return code
    
    def __len__(self):
        '''Get size of linked list'''
        return self.__size
    
    def __eq__(self, other: LinkedList):
        '''Check if two LinkedLists are the same when it comes to Node values.
        Use "is" if you want to compare whether they point to the same memory location'''
        if len(self) != len(other):
            return False
        
        for snode, onode in zip(self, other):
            if snode != onode:
                return False
        return True


    ## General list methods that aren't built in functions

    def is_empty(self) -> bool:
        '''Check if the linked list is empty'''
        return self.__size == 0

    def get_head(self) -> Node:
        '''Get first node'''
        return self.__head

    def get_tail(self) -> Node:
        '''Get last node'''
        return self.__tail

    def get(self, index: int) -> Node:
        '''Get node at index, returns none if index out of bounds'''
        if index < 0 or index >= len(self):
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

    def append(self, new_node: Node, extend_flag = False):
        '''Append to the end. Will be last node of the linked list'''
        if not extend_flag:
            new_node.set_next(None)

        if self.is_empty():
            self.__head = new_node
            self.__head.set_previous(None)
            self.__size = 1
            return
        
        if self.__tail is None: # aka the list has only one element (__head)
            self.__head.set_next(new_node)
            self.__tail = new_node
            self.__tail.set_previous(self.__head)
            self.__size = 2
            return
        
        self.__tail.set_next(new_node)
        new_node.set_previous(self.__tail)
        self.__tail = new_node
        self.__size += 1
    
    def prepend(self, new_node: Node, preextend_flag = False):
        '''Append to the front/start of the linked list'''
        if not preextend_flag:
            new_node.set_previous(None)

        if self.is_empty():
            self.__head = new_node
            self.__head.set_next(None)
            self.__size = 1
            return

        if self.__tail is None:
            self.__tail = self.__head
            self.__tail.set_previous(new_node)
            self.__head = new_node
            self.__head.set_next(self.__tail)
            self.__size = 2
            return
        
        self.__head.set_previous(new_node)
        new_node.set_next(self.__head)
        self.__head = new_node
        self.__size += 1

    def insert_before(self, insertion_point: Node, new_node: Node):
        '''Insert before a certain node. LinkedList < [...] new_node insertion_point [...] >'''
        if insertion_point is self.__head:
            self.prepend(new_node)
            return
        
        before_insertion_point = insertion_point.get_previous()
        
        new_node.set_previous(before_insertion_point)
        new_node.set_next(insertion_point)
        
        before_insertion_point.set_next(new_node)
        insertion_point.set_previous(new_node)
        self.__size += 1

    def insert_after(self, insertion_point: Node, new_node: Node):
        '''Insert after a certain node. LinkedList < [...] insertion_point new_node [...] >'''
        next_node_after_insertion = insertion_point.get_next()
        if next_node_after_insertion is None: # insertion_point was self.__tail (or self.__head when self.__size is 1)
            self.append(new_node)
        else:
            self.insert_before(next_node_after_insertion, new_node)

    def insert_at_index(self, index: int, new_node: Node):
        '''Insert the new node at index. LinkedList < [...] new_node previous_node_at_that_index [...] >'''
        insertion_point = self.get(index)
        if insertion_point is not None:
            self.insert_before(insertion_point, new_node)

    def extend(self, new_node: Node):
        '''Extends the link list with multiple Nodes already linked'''
        self.append(new_node, True)
        new_tail = self.__tail.get_next()
        while new_tail is not None:
            self.__tail = new_tail
            self.__size += 1
            new_tail = new_tail.get_next()

    def preextend(self, new_node: Node):
        '''Extends the front of the link list with multiple Nodes already linked'''
        self.prepend(new_node, True)
        new_head = self.__head.get_previous()
        while new_head is not None:
            self.__head = new_head
            self.__size += 1
            new_head = new_head.get_previous()


    # Removing/deleting

    def remove_head(self) -> Node:
        '''Remove the first node and return it'''
        old_head = self.__head
        if old_head is not None:
            self.__head = old_head.get_next()
            if self.__head is not None:
                self.__head.set_previous(None)
            old_head.set_next(None)
            self.__size -= 1

            if len(self) == 1:
                self.__tail = None
                self.__head.set_next(None)

        return old_head
    
    def remove_tail(self) -> Node: 
        '''Remove the last node and return it'''
        old_tail = self.__tail
        if old_tail is not None:
            self.__tail = old_tail.get_previous()
            self.__tail.set_next(None)
            old_tail.set_previous(None)
            self.__size -= 1

            if len(self) == 1:
                self.__tail = None
                self.__head.set_next(None)

        return old_tail

    def remove(self, node_to_remove: Node):
        '''Remove a specific node'''
        if node_to_remove is None:
            return
        
        if node_to_remove is self.__head:
            self.remove_head()
            return
        if node_to_remove is self.__tail:
            self.remove_tail()
            return
        
        if node_to_remove.get_next() is not None and node_to_remove.get_previous is not None:
            node_before_removed = node_to_remove.get_previous()
            node_after_removed = node_to_remove.get_next()
            node_before_removed.set_next(node_after_removed)
            node_to_remove.set_next(None)
            node_to_remove.set_previous(None)
            self.__size -= 1
            if len(self) == 1:
                self.__tail = None

    def remove_at_index(self, index: int) -> Node:
        '''Remove the node at index and return it, or return None if index out of bounds'''
        node_to_be_removed = self.get(index)
        
        if node_to_be_removed is not None:
            self.remove(node_to_be_removed)
        
        return node_to_be_removed

    def empty(self):
        '''Remove all nodes'''
        self.__head = None
        self.__tail = None
        self.__size = 0