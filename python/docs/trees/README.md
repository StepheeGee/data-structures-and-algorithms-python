# Trees - Implementation

Implementation of binary trees and binary search trees.

## Date - 1.26.24 (Challenge 15)

## Code

- [Binary Tree Code](../../data_structures/binary_tree.py)
- [Binary Search Tree Code](../../data_structures/binary_search_tree.py)

## Approach & Efficiency

### Binary Tree

The binary tree implementation includes a `Node` class and a `BinaryTree` class with depth-first traversal methods (pre-order, in-order, post-order). The approach involves recursive traversal, resulting in a time complexity of O(n) for each traversal method, where 'n' is the number of nodes in the tree. The space complexity is O(h), where 'h' is the height of the tree.

### Binary Search Tree

The binary search tree implementation extends the binary tree and includes additional methods for adding nodes and checking for the presence of a value. The `add` and `contains` methods have a time complexity of O(log n) on average, where 'n' is the number of nodes in the tree. The space complexity for these methods is also O(h), where 'h' is the height of the tree.

## Solution

To run the code, you can use the provided Python files in your project. Here's an example of how to use the binary search tree:

```python
from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
bst.add(10)
bst.add(5)
bst.add(15)
bst.add(3)
bst.add(7)

print(bst.pre_order())  # [10, 5, 3, 7, 15]
print(bst.in_order())   # [3, 5, 7, 10, 15]
print(bst.post_order()) # [3, 7, 5, 15, 10]

print(bst.contains(7))  # True
print(bst.contains(12)) # False
```

## Conclusion

This exercise demonstrates the implementation of binary trees and binary search trees in Python. It highlights the fundamental concepts of tree structures and their applications in organizing and searching data.

## Resources

- Python documentation: [https://docs.python.org/](https://docs.python.org/)
- Data Structures and Algorithms in Python by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser.
