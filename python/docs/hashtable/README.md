# Class 30: Hash Table Implementation

2.18.24

## Challenge Description

Implement a Hashtable class with the following methods:

- `set(key, value)`: Hashes the key and sets the key-value pair in the table, handling collisions as needed. If a given key already exists, it replaces its value with the provided value.
- `get(key)`: Retrieves the value associated with the given key.
- `has(key)`: Checks if the key exists in the table and returns a boolean indicating its presence.
- `keys()`: Returns a collection of all unique keys in the table.
- `hash(key)`: Computes the index in the collection for the given key.

## Approach & Efficiency

The Hashtable class utilizes separate chaining to handle collisions, and the hash function ensures efficient distribution of keys across the table. The time complexity for operations is O(1) on average, assuming a good hash function and a well-distributed set of keys.

## Solution & Usage

1. Import the `Hashtable` class into your Python script or interactive environment:

```python
from hashtable import Hashtable
```

2. Create an instance of the `Hashtable` class:

```python
my_hashtable = Hashtable()
```

3. Use the methods of the `Hashtable` class to interact with the hashtable:

```python
my_hashtable.set("key", "value")
result = my_hashtable.get("key")
print(result)  # Output: "value"
```

## Methods

### `__init__(self, size=10)`

Initialize the Hashtable with a specified size. If no size is provided, the default size is 10.

### `hash(self, key)`

Hash the given key to determine the index within the hashtable.

### `set(self, key, value)`

Set the key-value pair in the hashtable, handling collisions as needed. If the key already exists, replace its value.

### `get(self, key)`

Retrieve the value associated with the given key. Return `None` if the key is not found.

### `has(self, key)`

Check if the key exists in the hashtable. Return `True` if the key exists, `False` otherwise.

### `keys(self)`

Retrieve a collection of all unique keys in the hashtable.

## Running Tests

Ensure that `pytest` is installed:

```bash
pip install pytest
```

Run the tests using:

```bash
pytest test_hashtable.py
```

## Features

- **set(key, value)**: This method hashes the key and sets the key and value pair in the table, handling collisions as needed. If a given key already exists, it replaces its value from the value argument given to this method.
- **get(key)**: Returns the value associated with that key in the table.
- **has(key)**: Returns a boolean, indicating if the key exists in the table already.
- **keys()**: Returns a collection of keys.
- **hash(key)**: Returns the index in the collection for that key.

