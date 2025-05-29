#!/usr/local/bin/python
from linkedlist import *

print("==========================")
ll = LinkedList()
print("Action:", "created list")
print(f"Is empty: {ll.is_empty()}")
print(f"Size: {ll.size()}")
print(f"Head: {ll.get_head()}")
print(f"Tail: {ll.get_tail()}")
print(ll)
print("==========================")

ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
ll.append(Node(4))
ll.append(Node(5))
print("Action:", "append a few nodes")
print(f"Is empty: {ll.is_empty()}")
print(f"Size: {ll.size()}")
print(f"Head: {ll.get_head()}")
print(f"Tail: {ll.get_tail()}")
print(ll)

print("Print with for loop all node values:")
number = 0
for node in ll:
    print(f"#{number} {node}")
    number += 1
print("==========================")

print("Action:", "check nodes at indexes")
print(ll)
print(f"Node at index -1: {ll.get(-1)}")
print(f"Node at index 0: {ll.get(0)}")
print(f"Node at index 1: {ll.get(1)}")
print(f"Node at index 4: {ll.get(4)}")
print(f"Node at index 3: {ll.get(3)}")
print(f"Node at index 2: {ll.get(2)}")
print(f"Node at index 5: {ll.get(5)}")
print("==========================")
