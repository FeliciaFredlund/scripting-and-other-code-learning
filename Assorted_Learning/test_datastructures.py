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

    ## Check if __eq__ works on LinkedLists
    ll2 = LinkedList()
    for i in range(4):
        ll.append(Node(i))
        ll2.append(Node(i))

    print("Action:", "create ll2 and populate both ll and ll2 with nodes and compare\n")

    print(f"ll = {ll}")
    print(f"ll2 = {ll2}")
    print(f"ll == ll2 (should be True): {ll == ll2}")
    
    print(f"\nAdd another element to ll2")
    ll2.append(Node(4))
    print(f"ll = {ll}")
    print(f"ll2 = {ll2}")
    print(f"ll == ll2 (should be False): {ll == ll2}")
    
    print(f"\nMake ll and ll2 same length but with a different value nodes")
    ll2.remove_at_index(2)
    print(f"ll = {ll}")
    print(f"ll2 = {ll2}")
    print(f"ll == ll2 (should be False): {ll == ll2}")
    print("\n==========================\n")

    ## Check insertion methods
    print("Action:", "checking insertion methods\n")

    print(ll)
    print(f"Size: {len(ll)}")
    
    print("\nInsert new node Node(10) at index 1 (insert_at_index). Should be second element")
    ll.insert_at_index(1, Node(10))
    print(ll)
    print(f"Size: {len(ll)}")
    
    print("\nInsert new node Node(20) before the first node (insert_before). Should be first element")
    ll.insert_before(ll.get_head(), Node(20))
    print(ll)
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    
    print("\nInsert new node Node(30) before the tail node (insert_before). Should be second to last element")
    ll.insert_before(ll.get_tail(), Node(30))
    print(ll)
    print(f"Size: {len(ll)}")
    print(f"Tail: {ll.get_tail()}")

    print("\nInsert new node Node(40) after the tail node (insert_after). Should be the tail")
    ll.insert_after(ll.get_tail(), Node(40))
    print(ll)
    print(f"Size: {len(ll)}")
    print(f"Tail: {ll.get_tail()}")

    print("\nInsert new node Node(50) after the head node (insert_after). Should be the second element")
    ll.insert_after(ll.get_head(), Node(50))
    print(ll)
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print("\n==========================\n")

    ## Check if extend and preextend
    ll = LinkedList()
    ll.append(Node(0))
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))

    node = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node.set_next(node2)
    node2.set_previous(node)
    node2.set_next(node3)
    node3.set_previous(node2)

    print("Action:", "extend and preextend\n")

    print(ll)
    ll.extend(node)
    print(f"Extended ll with Node chain (10, 20, 30):")
    print(ll)
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")

    node = Node(100)
    node2 = Node(200)
    node3 = Node(300)
    node.set_next(node2)
    node2.set_previous(node)
    node2.set_next(node3)
    node3.set_previous(node2)

    ll.preextend(node3)
    print(f"Preextended ll with Node chain (100, 200, 300):")
    print(ll)
    print(f"Size: {len(ll)}")
    print(f"Head: {ll.get_head()}")
    print(f"Tail: {ll.get_tail()}")
    print("\n==========================\n")



if __name__ == "__main__":
    testLinkedList()