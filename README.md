!!!ATTENTION!!!
if you're a not developer or have not any idea what's Binary Search Tree, then it's README file for you,
otherwise just read BST's docsting and run only it.



Binary Search Tree Data Structure

How to start: To run the program the user should install colors.txt(example: $ pip install -r colors.txt) and run the final.py file



Short Description: A Binary Search Tree  is considered a data structure made up of nodes, like Linked Lists. 
These nodes are either null or have references (links) to other nodes. 
These ‘other’ nodes are child nodes, called a left node and right node. 
Nodes have values. 
These values determine where they are placed within the Binary Search Tree.

Similarly to a linked list, each node is referenced by only one other node, its parent (except for the root node). 
So we can say that each node in a Binary Search Tree is in itself a Binary Search Tree. Because further down the tree, we reach another node and that node has a left and a right. 
Then depending on which way we go, that node has a left and a right and so on.
1. The left node is always smaller than its parent.
2. The right node is always greater than its parent.
3. A Binary Search Tree is considered balanced if every level of the tree is fully filled with the exception of the last level. 
 On the last level, the tree is filled left to right.
4. A Perfect Binary Search Tree is one in which it is both full and complete.

Functions: 

1.insert (to insert an item in tree "first insertion will be the root")

2.preorder

3.inorder

4.postorder

5.levelorder

6.find (will return True if would find an item)

7.clear (to clear all tree)

8.erase (will delete an item)

9.height (will count height of the tree)

10.number of nodes (will count all nodes in tree)

11. to close the program type 0
