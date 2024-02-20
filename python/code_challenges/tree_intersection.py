from data_structures.binary_tree import BinaryTree

def tree_intersection(tree1, tree2):
    """
    Find common values in two binary trees.

    Args:
        tree1 (BinaryTree): The first binary tree.
        tree2 (BinaryTree): The second binary tree.

    Returns:
        set: A set containing the common values found in both trees.
    """
    # Create hash sets to store values of each tree
    values_set_tree1 = set()
    values_set_tree2 = set()

    # Helper function for depth-first traversal and adding values to sets
    def traverse_and_add(node, values_set):
        if node:
            values_set.add(node.value)
            traverse_and_add(node.left, values_set)
            traverse_and_add(node.right, values_set)

    # Traverse both trees and add values to respective sets
    traverse_and_add(tree1.root, values_set_tree1)
    traverse_and_add(tree2.root, values_set_tree2)

    # Find the intersection of the two sets
    common_values = values_set_tree1.intersection(values_set_tree2)

    return common_values
