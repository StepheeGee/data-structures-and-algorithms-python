import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "None"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_no_common_keys():
    synonyms = {
        "happy": "joyful",
        "bright": "shiny",
        "fast": "quick",
    }
    antonyms = {
        "sad": "unhappy",
        "dark": "dim",
        "slow": "leisurely",
    }

    expected = [
        ["happy", "joyful", "None"],
        ["bright", "shiny", "None"],
        ["fast", "quick", "None"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_empty_input():
    synonyms = {}
    antonyms = {}

    expected = []

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_same_keys_different_values():
    synonyms = {
        "happy": "joyful",
        "bright": "shiny",
        "fast": "quick",
    }
    antonyms = {
        "happy": "unhappy",
        "bright": "dim",
        "fast": "slow",
    }

    expected = [
        ["happy", "joyful", "unhappy"],
        ["bright", "shiny", "dim"],
        ["fast", "quick", "slow"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
