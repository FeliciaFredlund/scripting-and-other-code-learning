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

Preorder: [4, 2, 1, 7, 6] It's called "preorder" because the current node is visited before its children.
Postorder: [1, 2, 6, 7, 4]  It's called "postorder" because the current node is visited after its children. 
Inorder: [1, 2, 4, 6, 7] It's called "inorder" because the current node is visited between its children.

## Red Black Tree
A self-balancing binary tree using colors. When inserting, always set the new node to red. After insertion, do a recolor of the tree and rotations as needed.

- Each node is either red or black.
- The root is black.
- All Nil leaf nodes are black.
**- If a node is red, then both its children are black.**
- All paths from a single node go through the same number of black nodes to reach any of its descendant Nil (black) nodes.

When rotating left:
- The "pivot" node's initial parent becomes its left child
- The "pivot" node's old left child becomes its initial parent's new right child

When rotating right:
- The "pivot" node's initial parent becomes its right child
- The "pivot" node's old right child becomes its initial parent's new left child

## Hashmap
A data structure that maps keys to values. Hashmaps are made up of arrays on the backend (or lists in Python). The key hashes down to the index which is where the key and value is stored. So you need a hashing algorithm with few collisions, and/or built in functionality to handle collisions (this is what actually happens).

## Try/Tries
A tree used for storing and searching words efficiently. A trie is also often referred to as a "prefix tree" because it can be used to efficiently find all of the words that start with a given prefix. In Python, a trie is easily implemented as a nested tree of dictionaries where each key is a character that maps to the next character in a word.

hello and hi. * as end symbol
```py
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}
```

From wikipedia:
> In computer science, a trie (/ˈtraɪ/, /ˈtriː/ ⓘ), also known as a digital tree or prefix tree,[1] is a specialized search tree data structure used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. Instead, each node's position within the trie determines its associated key, with the connections between nodes defined by individual characters rather than the entire key.
> Tries are particularly effective for tasks such as autocomplete, spell checking, and IP routing, offering advantages over hash tables due to their prefix-based organization and lack of hash collisions. Every child node shares a common prefix with its parent node, and the root node represents the empty string. While basic trie implementations can be memory-intensive, various optimization techniques such as compression and bitwise representations have been developed to improve their efficiency. A notable optimization is the radix tree, which provides more efficient prefix-based storage.

## Graph
A collection of nodes connected by edges. Nodes are often called vertex/vertices.
A graph is a tree. Or more specifically, all trees are graphs, but not all graphs are trees.
Can be represented by a matrix (list of lists that hold True/False), or a hashmap where each key hold a set/list with the vertices it has edges with.