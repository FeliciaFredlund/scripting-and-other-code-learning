#!/usr/local/bin/python

def testLinkedList():
    '''Testing the linked list data structure I coded in linkedlist.py'''
    
    from linkedlist import LinkedList, Node

    print("==========================\n")

    ## Setting up an empty linked list and checking basic functions
    ll = LinkedList()
    print("Action:", "create empty list\n")

    print(ll)
    print(repr(ll))
    print(f"Is empty: {ll.is_empty()}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")
    print("\n==========================\n")

    ## Appending some nodes and checking basic functions
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    ll.append(Node(4))
    ll.append(Node(5))

    print("Action:", "append 5 nodes (1, 2, 3, 4, 5)\n")

    print(ll)
    print(repr(ll))
    print(f"Is empty: {ll.is_empty()}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")

    print("Print with for loop all node values:")
    number = 0
    for node in ll:
        print(f"#{number} {node}")
        number += 1
    print("\n==========================\n")

    ## Checking .get() method of
    print("Action:", "check nodes at indexes\n")

    print(ll)
    print(f"Node at index -1: {ll.get(-1)}")
    print(f"Node at index 0: {ll.get(0)}")
    print(f"Node at index 1: {ll.get(1)}")
    print(f"Node at index 2: {ll.get(2)}")
    print(f"Node at index 3: {ll.get(3)}")
    print(f"Node at index 4: {ll.get(4)}")
    print(f"Node at index 5: {ll.get(5)}")
    print("\n==========================\n")

    ## Check if empty() works
    ll.empty()
    
    print("Action:", "empty the list with empty()\n")

    print(ll)
    print(f"Is empty: {ll.is_empty()}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")
    print("\n==========================\n")

    ## Check if prepending works as intended
    ll.prepend(Node(1))
    ll.prepend(Node(2))
    ll.prepend(Node(3))
    
    print("Action:", "make a new list and prepend 1, 2, 3\n")

    print(ll)
    print(f"Is empty: {ll.is_empty()}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")
    print("\n==========================\n")

    ## Check if remove_tail and remove_head works as intended
    old_head = ll.remove_head()
    old_tail = ll.remove_tail()

    print("Action:", "remove head and tail from current list, only 2 should be left\n")

    print(ll)
    print(f"Old head: {old_head}")
    print(f"Old tail: {old_tail}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")
    print("\n==========================\n")

    ## Check if remove_at_index() works with a list starting at 3 items, removing mid item, tail and head
    ll.append(Node(3))
    ll.prepend(Node(1))

    print("Action:", "test remove_at_index for deleting in the middle item, tail and then head\n")

    print(ll)
    old_node = ll.remove_at_index(1)
    print(f"Old node at previous index 1: {old_node}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")

    print(ll)
    old_node = ll.remove_at_index(1)
    print(f"Old node at previous index 1: {old_node}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")

    print(ll)
    old_node = ll.remove_at_index(0)
    print(f"Old node at previous index 0: {old_node}")
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")
    print(ll)
    print("\n==========================\n")

    ## Check if Nodes __eq__ work as intended
    node = Node(10)
    node2 = Node(10)

    print("Action:", "made two Node(10) and will compare them\n")

    print(f"Compare node's and node2's values. node == node2 (should be True): {node == node2}")
    print(f"Compare node's value to 10. node == 10 (should be True): {node == 10}")
    node2.set_value(11)
    print(f"Change node2's value to 11 and compare again. node == node2 (should be False): {node == node2}")
    print(f"Compare node's value to 11. node == 11 (should be False): {node == 11}")
    print("\n==========================\n")


if __name__ == "__main__":
    testLinkedList()