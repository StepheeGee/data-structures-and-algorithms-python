# linked_list_insertions/insertion.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target_value, new_value):
        # Create a new node with the specified value
        new_node = Node(new_value)

        # Check if the linked list is empty
        if not self.head:
            raise TargetError("Cannot insert before in an empty list")

        # Check if the target value is at the beginning of the list
        if self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the linked list to find the node with the target value
        current = self.head
        while current.next and current.next.value != target_value:
            current = current.next

        # If the target value is not found in the list
        if not current.next:
            raise TargetError(f"Target value '{target_value}' not found in the list")

        # Insert the new node before the node with the target value
        new_node.next = current.next
        current.next = new_node


    def insert_after(self, target_value, new_value):
            new_node = Node(new_value)
            if not self.head:
                raise TargetError("Cannot insert after in an empty list")

            current = self.head
            while current and current.value != target_value:
                current = current.next

            if not current:
                raise TargetError(f"Target value '{target_value}' not found in the list")

            new_node.next = current.next
            current.next = new_node

    def __str__(self):
            result = ""
            current = self.head
            while current:
                result += f"{{ {current.value} }} -> "
                current = current.next
            result += "NULL"
            return result

class TargetError(Exception):
        pass
