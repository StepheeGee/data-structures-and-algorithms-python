class Node:
    """Node class for a binary tree."""
    def __init__(self, value):
        """
        Initialize a new node.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """BinaryTree class with depth-first traversal methods."""
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def pre_order(self):
        """
        Perform pre-order traversal of the binary tree.

        Returns:
            List: A list of values ordered in pre-order.
        """
        result = []
        def traverse(node):
            if node:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return result

    def in_order(self):
        """
        Perform in-order traversal of the binary tree.

        Returns:
            List: A list of values ordered in in-order.
        """
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)
        traverse(self.root)
        return result

    def post_order(self):
        """
        Perform post-order traversal of the binary tree.

        Returns:
            List: A list of values ordered in post-order.
        """
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.value)
        traverse(self.root)
        return result

    def find_maximum_value(self):
        max_value = None
        if self.root:
            values = self.pre_order()
            # Find the maximum value
            max_value = max(values)
        return max_value




