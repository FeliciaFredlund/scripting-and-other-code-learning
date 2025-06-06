# Descriptions of All Data Structures

Here I will have a short-ish description of each data structure (taking from boot.dev or wikipedia or own words). I'm doing this so I can try implementing the data structures myself whenever I feel like it without having to look up descriptions which might give hints in how to do it.

There is array in python. Need to "import array" though.

## Stack
Last in, first out.
Has a push, pop, size function. Is like a stack of plates. Add to the top, take from the top.
It also has peek, which returns the first item without removing it.

## Queue
First in, first out.
Items are added to the tail and removed from the head.
Methods: enqueue (add to queue), dequeue (remove from the queue), peek (looks at the item about to be removed)

## Linked List
A chain of nodes, efficient for inserts and deletes.
A linked list is where elements are not stored next to each other in memory, instead, each item references the next in a chain.
Wikipedia: A linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence. In its most basic form, each node contains data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions.
A basic linked list only hold the next node in the sequence; a doubly linked list also holds the previous node in the sequence. Keeping track of the tail as well as the head seems to be a choice.

## Binary Tree
A tree where each node has up to two children, and only one parent. A Binary Search Tree is a sorted binary tree, that is a data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. 

1. Instead of an unbounded list of children, each node has at most 2 children
2. The left child's value must be less than its parent's value
3. The right child's value must be greater than its parent's value
4. No two nodes in the BST can have the same value

Add/insert (self balancing or not??!?!?!?!), remove, search (node exists), get_min, get_max, preorder_traversal (Sometimes it's useful (albeit a bit slow) to iterate over all the nodes in the tree. A "preorder" traversal is a way to visit all the nodes in a tree. It's called "preorder" because the current node is visited before its children. Recursive?!?), postorder_traversal (A "postorder" traversal also visits all the nodes in a tree. It's called "postorder" because the current node is visited after its children. Recursive?!), inorder_traversal (An "inorder" traversal is the most intuitive way to visit all the nodes in a tree. It's called "inorder" because the current node is visited between its children. Recursive?!), height

     4
 2       7
1       6

Preorder: [4, 2, 1, 7, 6]
Postorder: [1, 2, 6, 7, 4]
Inorder: [1, 2, 4, 6, 7]

## Red Black Tree
A self-balancing binary tree using colors.

## Hashmap
A data structure that maps keys to values.

## Try/Tries
A tree used for storing and searching words efficiently.

## Graph
A collection of nodes connected by edges.
