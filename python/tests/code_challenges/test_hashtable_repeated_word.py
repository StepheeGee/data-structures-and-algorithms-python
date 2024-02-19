import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word


# @pytest.mark.skip("TODO")
def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected
    

# @pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected

def test_numbers_and_symbols():
    actual = first_repeated_word("123 abc !@# 456 abc 789")
    expected = "abc"
    assert actual == expected

def test_mixed_case_repeated():
    actual = first_repeated_word("Hello World hello world")
    expected = "hello"
    assert actual == expected

def test_mixed_case_different_words():
    actual = first_repeated_word("Hello World python")
    expected = None
    assert actual == expected

def test_repeated_words_with_spaces():
    actual = first_repeated_word("apple     banana    apple")
    expected = "apple"
    assert actual == expected

def test_repeated_words_with_tabs():
    actual = first_repeated_word("apple\tbanana\tapple")
    expected = "apple"
    assert actual == expected

def test_repeated_words_mixed_whitespace():
    actual = first_repeated_word("apple \t banana  apple")
    expected = "apple"
    assert actual == expected


