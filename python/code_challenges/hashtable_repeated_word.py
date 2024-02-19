import string
from data_structures.hashtable import Hashtable

def remove_punctuation(word):
    """
    Helper function to remove punctuation from a word.
    """
    return word.translate(str.maketrans("", "", string.punctuation))

def first_repeated_word(input_string):
    """
    Find the first word to occur more than once in a string using a Hashtable.

    :param input_string: The input string to search for repeated words.
    :type input_string: str
    :return: The first repeated word, or None if no repeated word is found.
    :rtype: str or None
    """
    # Create an instance of Hashtable
    hashtable = Hashtable()

    # Split the input string into words and remove punctuation
    words = [remove_punctuation(word.lower()) for word in input_string.split()]

    for word in words:
        # Check if the word is already in the hashtable, if yes, return it as the first repeated word
        if hashtable.has(word):
            return word
        else:
            # Otherwise, add the lowercase word to the hashtable
            hashtable.set(word, True)

    # If no repeated word is found, return None
    return None


