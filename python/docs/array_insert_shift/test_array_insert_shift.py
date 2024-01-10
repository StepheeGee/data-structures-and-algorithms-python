import pytest

def insertShiftArray(arr, value):
    new_array = []
    mid = len(arr) // 2

    for i in range(len(arr) + 1):
        if i == mid:
            new_array.append(value)
        elif i < mid:
            new_array.append(arr[i])
        else:
            new_array.append(arr[i - 1])

    return new_array



def test_insertShiftArray():
    # Test case 1
    arr1 = [2, 4, 6, -8]
    val1 = 5
    expected1 = [2, 4, 5, 6, -8]
    assert insertShiftArray(arr1, val1) == expected1

    # Test case 2
    arr2 = [42, 8, 15, 23, 42]
    val2 = 16
    expected2 = [42, 8, 16, 15, 23, 42]
    assert insertShiftArray(arr2, val2) == expected2

    # Test case 3
    arr3 = [1, 2, 3, 4, 5]
    val3 = 6
    expected3 = [1, 2, 6, 3, 4, 5]
    assert insertShiftArray(arr3, val3) == expected3



# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])

