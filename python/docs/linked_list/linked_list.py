class Node:
    """
    A class representing a node in a linked list.

    Attributes:
    - value: The value stored in the node.
    - next: A reference to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Parameters:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
    - head: The head (first node) of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the head of the linked list.

        Parameters:
        - value: The value to be inserted into the linked list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """
        Checks if a node with the given value exists in the linked list.

        Parameters:
        - value: The value to be searched for in the linked list.

        Returns:
        - True if the value exists, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        - A string representing all the values in the linked list, formatted as:
          "{ a } -> { b } -> { c } -> NULL"
        """
        result = ""
        current = self.head
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result

# Example usage:
linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)

print(linked_list.includes(2))  # True
print(linked_list.includes(4))  # False

print(linked_list)  # "{ 1 } -> { 2 } -> { 3 } -> NULL"




class TargetError:
    pass


#pytest -k linked_list


