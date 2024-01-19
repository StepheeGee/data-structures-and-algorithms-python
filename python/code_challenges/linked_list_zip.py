class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

def zip_lists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    current1, current2 = list1.head, list2.head
    while current1 and current2:
        temp1, temp2 = current1.next, current2.next
        current1.next = current2
        current2.next = temp1

        current1, current2 = temp1, temp2

    if current2:
        # Append remaining elements from list2
        current = list1.head
        while current.next:
            current = current.next
        current.next = current2

    return list1
