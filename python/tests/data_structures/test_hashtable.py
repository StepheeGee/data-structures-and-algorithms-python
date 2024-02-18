import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected



def test_set_get():
    hashtable = Hashtable()
    hashtable.set("one", 1)
    assert hashtable.get("one") == 1

def test_nonexistent_key():
    hashtable = Hashtable()
    assert hashtable.get("nonexistent") is None

def test_unique_keys():
    hashtable = Hashtable()
    hashtable.set("one", 1)
    hashtable.set("two", 2)
    hashtable.set("three", 3)
    assert set(hashtable.keys()) == {"one", "two", "three"}

def test_collision_handling():
    hashtable = Hashtable(size=2)  # Force a small table size to induce collisions
    hashtable.set("neo", 5)
    hashtable.set("oen", 6)
    assert hashtable.get("neo") == 5
    assert hashtable.get("oen") == 6

def test_hash_in_range():
    hashtable = Hashtable(size=100)
    key = "example"
    hashed_index = hashtable.hash(key)
    assert 0 <= hashed_index < 100
