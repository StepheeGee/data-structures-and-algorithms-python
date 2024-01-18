class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class TargetError(Exception):
    pass

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k should be a non-negative integer")

        slow_ptr = fast_ptr = self.head

        # Move fast_ptr k nodes ahead
        for _ in range(k):
            if fast_ptr is None:
                raise TargetError("k is greater than or equal to the length of the linked list")
            fast_ptr = fast_ptr.next

        # Check if fast_ptr is None, meaning k is equal to the length of the linked list
        if fast_ptr is None:
            raise TargetError("k is greater than or equal to the length of the linked list")

        # Move both pointers until fast_ptr reaches the end
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        # At this point, slow_ptr is k nodes from the end
        return slow_ptr.value
