# Hashtable - Repeated Word

Code Challenge 31 is to Find the first repeated word in a book.

Date: 2.19.24

## Whiteboard Process

[Whiteboard](Hashmap.png)

[Code](../../code_challenges/hashtable_repeated_word.py)

## Approach & Efficiency

### Approach

The code utilizes a Hashtable to efficiently find the first repeated word in a given string. The approach involves removing punctuation, converting words to lowercase for case-insensitive comparison, and storing unique words in the Hashtable. The algorithm iterates through the words, checking for repeats using the Hashtable.

### Efficiency

- **Time Complexity**: The time complexity of the algorithm is O(N), where N is the number of words in the input string. This is because each word is processed once, and Hashtable operations like set and has are generally O(1).

- **Space Complexity**: The space complexity is also O(N), where N is the number of unique words in the input string. The Hashtable stores each unique word.

## Solution

### Running the Code

To run the code, follow these steps:

1. Make sure you have the required files and dependencies.
2. Use the `first_repeated_word` function by providing a string as an argument.

```python
from code_challenges.hashtable_repeated_word import first_repeated_word

input_string = "Your input string goes here."
result = first_repeated_word(input_string)

print(f"The first repeated word is: {result}")
```

### Examples

Example 1:
```python
input_string = "apple banana apple"
result = first_repeated_word(input_string)
# Output: "apple"
```

Example 2:
```python
input_string = "The quick brown fox jumps over the lazy dog."
result = first_repeated_word(input_string)
# Output: None (No repeated words)
```

## Practical Purpose

The practical purpose of this code is to efficiently identify the first repeated word in a given text. It is designed with simplicity and readability in mind, making it suitable for various applications, including:

- Spell-checking: Identifying repeated words can help catch potential spelling errors.
- Text analysis: Detecting common terms or phrases in large texts.
- Data cleaning: Preprocessing textual data to identify duplicate words.

This solution provides a foundation for handling textual data and can be integrated into larger projects or applications where identifying repeated words is valuable.
