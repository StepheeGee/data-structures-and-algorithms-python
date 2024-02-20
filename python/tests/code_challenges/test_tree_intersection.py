import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)


# @pytest.mark.skip("TODO")
def test_tree_intersection_basic():

    tree_a = BinaryTree()
    values_a = [1, 2, 3, 4, 5]
    add_values_to_empty_tree(tree_a, values_a)

    tree_b = BinaryTree()
    values_b = [6, 7, 8, 9, 10]
    add_values_to_empty_tree(tree_b, values_b)

    actual = tree_intersection(tree_a, tree_b)
    expected = set()

    assert set(actual) == expected

def test_tree_intersection_common_values():

    tree_a = BinaryTree()
    values_a = [1, 2, 3, 4, 5]
    add_values_to_empty_tree(tree_a, values_a)

    tree_b = BinaryTree()
    values_b = [3, 4, 5, 6, 7]
    add_values_to_empty_tree(tree_b, values_b)

    actual = tree_intersection(tree_a, tree_b)
    expected = {3, 4, 5}

    assert set(actual) == expected

def test_tree_intersection_duplicate_values():

    tree_a = BinaryTree()
    values_a = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    add_values_to_empty_tree(tree_a, values_a)

    tree_b = BinaryTree()
    values_b = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    add_values_to_empty_tree(tree_b, values_b)

    actual = tree_intersection(tree_a, tree_b)
    expected = {1, 2, 3, 4, 5}

    assert set(actual) == expected
