# data_structures/stack.py
from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    """
    Node Class:
    Represents a node in a linked list.

    Attributes:
    - value: The value stored in the node.
    - next: A pointer to the next node in the linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    Stack Class:
    Represents a stack data structure using a linked list.

    Attributes:
    - top: The top node of the stack.

    Methods:
    - push(value): Adds a new node with the given value to the top of the stack.
    - pop(): Removes and returns the value from the top of the stack.
    - peek(): Returns the value of the node located at the top of the stack without removing it.
    - is_empty(): Returns True if the stack is empty, False otherwise.
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Adds a new node with the given value to the top of the stack.

        Args:
        - value: The value to be added to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the value from the top of the stack.

        Returns:
        - The value of the node removed from the top of the stack.

        Raises:
        - InvalidOperationError: If called on an empty stack.
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Returns the value of the node located at the top of the stack without removing it.

        Returns:
        - The value of the node at the top of the stack.

        Raises:
        - InvalidOperationError: If called on an empty stack.
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return self.top is None






