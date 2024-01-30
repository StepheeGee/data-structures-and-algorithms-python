# Tree Max (Code Challenge 16)

**Date: 1.29.24**

## Description

This code challenge involves the implementation of a method for the Binary Tree class to find the maximum value within the tree.

## Binary Tree Class

The `BinaryTree` class is equipped with the following methods:

- `pre_order`: Performs pre-order traversal of the binary tree and returns a list of values in pre-order.
- `in_order`: Performs in-order traversal of the binary tree and returns a list of values in in-order.
- `post_order`: Performs post-order traversal of the binary tree and returns a list of values in post-order.
- `find_maximum_value`: Finds and returns the maximum value in the binary tree.

## Node Class

The `Node` class represents a node in a binary tree. Each node contains a value and references to its left and right children.

## Test Cases

A test case is provided to verify the correctness of the `find_maximum_value` method. The test case creates a binary tree with specific values and asserts that the maximum value is correctly identified.

## Whiteboard Process

A whiteboard illustration is included to visualize the approach and structure of the code.

![whiteboard](binarytree.jpg)

[binary_tree.py](../../data_structures/binary_tree.py)

## Approach & Efficiency

### Approach

The `find_maximum_value` method utilizes pre-order traversal to obtain a list of all values in the tree and then finds the maximum value from that list.

### Efficiency

- **Time Complexity:**
  - The time complexity of the `find_maximum_value` method is O(N), where N is the number of nodes in the binary tree. This is because the method traverses each node exactly once.

- **Space Complexity:**
  - The space complexity is O(N) as well. This is due to the space required for the list of values obtained during pre-order traversal. In the worst case, this list will contain all the values of the nodes.

## Solution

The solution is implemented in the [binary_tree.py](../../data_structures/binary_tree.py) file. The `find_maximum_value` method can be used to find the maximum value in a binary tree.

Example:

```python
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(30)
tree.root.right = Node(-7)

max_value = tree.find_maximum_value()
print(max_value)  # Output: 30
```

Note: The provided whiteboard, code, and explanations are intended to serve as a guide, and additional testing and analysis may be necessary for a complete understanding of the code.
