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

## Binary Tree
A tree where each node has up to two children.

## Red Black Tree
A self-balancing binary tree using colors.

## Hashmap
A data structure that maps keys to values.

## Try/Tries
A tree used for storing and searching words efficiently.

## Graph
A collection of nodes connected by edges.
