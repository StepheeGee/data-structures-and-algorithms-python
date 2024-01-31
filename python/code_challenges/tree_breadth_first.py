from data_structures.binary_tree import BinaryTree

def breadth_first(tree):
    """
    Perform breadth-first traversal of the binary tree.

    Args:
        tree (BinaryTree): The binary tree to traverse.

    Returns:
        List: A list of values ordered in breadth-first.
    """
    result = []
    if not tree.root:
        return result

    queue = [tree.root]
    front = 0  # Pointer to the front of the queue
    rear = 1   # Pointer to the rear of the queue

    while front < rear:
        current_node = queue[front]
        front += 1
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
            rear += 1
        if current_node.right:
            queue.append(current_node.right)
            rear += 1

    return result

