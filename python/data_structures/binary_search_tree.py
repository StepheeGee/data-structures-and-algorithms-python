from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """BinarySearchTree class, a subclass of BinaryTree with additional methods."""
    def add(self, value):
        """
        Add a new node with the given value to the binary search tree.

        Args:
            value: The value to be added to the tree.
        """
        self.root = self._add_node(self.root, value)

    def _add_node(self, node, value):
        """
        Helper function to recursively add a new node with the given value.

        Args:
            node: The current node in the recursion.
            value: The value to be added.

        Returns:
            Node: The updated node.
        """
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._add_node(node.left, value)
        elif value > node.value:
            node.right = self._add_node(node.right, value)

        return node

    def contains(self, value):
        """
        Check if the binary search tree contains the given value.

        Args:
            value: The value to be checked.

        Returns:
            bool: True if the value is in the tree, False otherwise.
        """
        return self._contains_node(self.root, value)

    def _contains_node(self, node, value):
        """
        Helper function to recursively check if the tree contains the given value.

        Args:
            node: The current node in the recursion.
            value: The value to be checked.

        Returns:
            bool: True if the value is in the tree, False otherwise.
        """
        if not node:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._contains_node(node.left, value)
        else:
            return self._contains_node(node.right, value)

 
