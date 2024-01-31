from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(kary_tree):
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    def transform_tree(node):
        if not node:
            return None

        new_node = Node(fizz_buzz(node.value))
        new_node.children = [transform_tree(child) for child in node.children]
        return new_node

    if not kary_tree.root:
        return KaryTree()

    new_tree = KaryTree(transform_tree(kary_tree.root))

    return new_tree
