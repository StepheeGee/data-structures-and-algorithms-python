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


class Queue:
    """
    Queue Class:
    Represents a queue data structure using a linked list.

    Attributes:
    - front: The front node of the queue.
    - rear: The rear node of the queue.

    Methods:
    - enqueue(value): Adds a new node with the given value to the back of the queue.
    - dequeue(): Removes and returns the value from the front of the queue.
    - peek(): Returns the value of the node located at the front of the queue without removing it.
    - is_empty(): Returns True if the queue is empty, False otherwise.
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Adds a new node with the given value to the back of the queue.

        Args:
        - value: The value to be added to the queue.
        """
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Removes and returns the value from the front of the queue.

        Returns:
        - The value of the node removed from the front of the queue.

        Raises:
        - InvalidOperationError: If called on an empty queue.
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        """
        Returns the value of the node located at the front of the queue without removing it.

        Returns:
        - The value of the node at the front of the queue.

        Raises:
        - InvalidOperationError: If called on an empty queue.
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        """
        return self.front is None



