# Stack Queue Animal Shelter

1.23.24

First-in, First-out Animal Shelter.

## Whiteboard Process

![Stack Queue Animal Shelter](AnimalShelter.jpg)

## Approach & Efficiency

### Approach

The algorithm utilizes a queue data structure to manage dogs and cats separately. Enqueue operations are based on species, and dequeue operations can be either based on preference (dog or cat) or the oldest animal in the shelter.

### Efficiency

- Enqueue Operation: O(1)
- Dequeue Operation (Any): O(1)
- Dequeue Operation (Dog or Cat): O(1)
- Dequeue Dog Operation: O(1)
- Dequeue Cat Operation: O(1)

The algorithm is designed for efficiency in both enqueuing and dequeuing operations.

## Solution

### How to Run the Code

1. Ensure you have the necessary data structures (`Queue` and `InvalidOperationError`) in the `data_structures` directory.
2. Import the `AnimalShelter` class along with `Dog` and `Cat` classes into your code.
3. Create an instance of `AnimalShelter`.
4. Use the `enqueue` method to add animals to the shelter.
5. Use the `dequeue` method to retrieve animals based on preference or arrival order.

### Examples

```python
from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError
from stack_queue_animal_shelter import AnimalShelter, Dog, Cat

# Example Usage
shelter = AnimalShelter()

# Enqueue a cat named "Felix"
cat = Cat("Felix")
shelter.enqueue(cat)

# Dequeue a cat
dequeued_cat = shelter.dequeue("cat")
print(f"Dequeued Cat: {dequeued_cat.name}")  # Output: "Dequeued Cat: Felix"
