class Hashtable:
    """
    Basic implementation of a Hashtable with methods for setting, getting, checking existence, retrieving keys, and hashing keys.
    """

    def __init__(self, size=10):
        """
        Initialize the Hashtable with a given size.

        :param size: Size of the hashtable.
        """
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        """
        Hash the given key to an index within the table.

        :param key: Key to be hashed.
        :return: Hashed index.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Set the key-value pair in the table, handling collisions as needed.

        :param key: Key to be set.
        :param value: Value to be associated with the key.
        :return: None
        """
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        """
        Retrieve the value associated with the given key.

        :param key: Key to be looked up.
        :return: Value associated with the key, or None if not found.
        """
        index = self.hash(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        return None

    def has(self, key):
        """
        Check if the key exists in the table.

        :param key: Key to be checked.
        :return: True if key exists, False otherwise.
        """
        index = self.hash(key)
        if self.table[index] is not None:
            for existing_key, _ in self.table[index]:
                if existing_key == key:
                    return True
        return False

    def keys(self):
        """
        Retrieve a collection of all unique keys in the hashtable.

        :return: List of keys.
        """
        result = set()
        for bucket in self.table:
            if bucket is not None:
                result.update(key for key, _ in bucket)
        return list(result)
