from data_structures.queue import Queue

def multi_bracket_validation(s):
    """
    Validates the balance of brackets in a given string.

    Args:
        s (str): The input string containing brackets.

    Returns:
        bool: True if brackets are balanced, False otherwise.
    """
    stack = []  # Stack to keep track of opening brackets
    brackets_map = {')': '(', ']': '[', '}': '{'}  # Mapping of closing to opening brackets

    for char in s:
        if char in brackets_map.values():
            stack.append(char)  # Push opening bracket onto the stack
        elif char in brackets_map:
            # Check if closing bracket matches the corresponding opening bracket on top of the stack
            if not stack or stack.pop() != brackets_map[char]:
                return False  # Unmatched brackets, return False

    return not stack  # If stack is empty, brackets are balanced, return True

