from data_structures.stack import Stack

class PseudoQueue:
    """
    A class representing a PseudoQueue using two Stacks.

    The PseudoQueue follows the first-in, first-out (FIFO) principle, where elements are
    enqueued at the rear and dequeued from the front.
    """

    def __init__(self):
        """
        Initialize the PseudoQueue with two empty stacks.
        """
        self.stack1 = Stack()  # Stack for enqueue operation (rear of the queue)
        self.stack2 = Stack()  # Stack for dequeue operation (front of the queue)

    def enqueue(self, value):
        """
        Enqueue a value into the PseudoQueue.

        Args:
        - value: The value to be enqueued.

        The enqueue operation adds a new element to the rear of the PseudoQueue.
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        Dequeue a value from the PseudoQueue.

        Returns:
        - The value dequeued from the PseudoQueue.

        The dequeue operation removes and returns the element from the front of the PseudoQueue.
        If the second stack is empty, elements are transferred from the first stack to the second stack
        to maintain the correct order.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
