# Stacks and Queues

## Feature

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue


## Whiteboard Process

Not Required

## Approach & Efficiency

The implementation uses a linked list as the underlying data storage mechanism for both the Stack and Queue. This choice allows for efficient operations such as push, pop, enqueue, and dequeue with O(1) time complexity.

### The Stack:

- **push:** Adds a new node to the top of the stack, O(1).
- **pop:** Removes and returns the value from the top of the stack, O(1).
- **peek:** Returns the value of the node at the top of the stack without removing it, O(1).
- **is_empty:** Checks if the stack is empty, O(1).

### The Queue:

- **enqueue:** Adds a new node to the back of the queue, O(1).
- **dequeue:** Removes and returns the value from the front of the queue, O(1).
- **peek:** Returns the value of the node at the front of the queue without removing it, O(1).
- **is_empty:** Checks if the queue is empty, O(1).

## Solution

To run the code, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Run the appropriate test file (e.g., `pytest tests/data_structures/test_stack.py`).

### Stack Example:

```python
# Import the Stack class
from data_structures.stack import Stack

# Instantiate a new stack
stack = Stack()

# Push values onto the stack
stack.push("apple")
stack.push("banana")
stack.push("cucumber")

# Visual representation of the stack:
#  _______________________________________
# | cucumber |   banana   |   apple    |
# |__________|____________|____________|
#    Top
```

Now, let's perform some operations:

```python
# Peek the top value
top_value = stack.peek()
print(f"Peeked value: {top_value}")

# Pop the top value
popped_value = stack.pop()
print(f"Popped value: {popped_value}")

# Visual representation after peek and pop:
#  _______________________
# |   banana   |   apple  |
# |____________|__________|
#      Top
```

### Queue Example:

```python
# Import the Queue class
from data_structures.queue import Queue

# Instantiate a new queue
queue = Queue()

# Enqueue values into the queue
queue.enqueue("apple")
queue.enqueue("banana")
queue.enqueue("cucumber")

# Visual representation of the queue:
#    _______________________
#   |   apple    |  banana  |  cucumber  |
#   |____________|__________|____________|
#   Front                        Rear
```

Now, let's perform some operations:

```python
# Peek into the queue
front_value = queue.peek()
print(f"Front value: {front_value}")

# Dequeue from the queue
dequeued_value = queue.dequeue()
print(f"Dequeued value: {dequeued_value}")

# Visual representation after peek and dequeue:
#    _________________
#   |   banana   |  cucumber  |
#   |____________|____________|
#   Front                        Rear
```


## Tests

The tests cover the functionality as follows:

### For the Stack:

1. `test_push_onto_empty`: Successfully pushes onto a stack.
2. `test_push_onto_full`: Successfully pushes multiple values onto a stack.
3. `test_pop_single`: Successfully pops off the stack.
4. `test_pop_until_empty`: Successfully empties a stack after multiple pops.
5. `test_peek`: Successfully peeks the next item on the stack.
6. `test_exists`: Successfully instantiates an empty stack.
7. `test_peek_empty` and `test_pop_empty`: Prove that calling pop or peek on an empty stack raises an exception (`InvalidOperationError`).

### For the Queue:

1. `test_enqueue`: Successfully enqueues into a queue.
2. `test_enqueue_two`: Successfully enqueues multiple values into a queue.
3. `test_dequeue`: Successfully dequeues out of a queue the expected value.
4. `test_peek`: Successfully peeks into a queue, seeing the expected value.
5. `test_exhausted`: Successfully empties a queue after multiple dequeues.
6. `test_exists`: Successfully instantiates an empty queue.
7. `test_dequeue_when_empty` and `test_peek_when_empty`: Prove that calling dequeue or peek on an empty queue raises an exception (`InvalidOperationError`).


