def reverseArray(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

#Example:
original_array = [1, 2, 3, 4, 5]
reversed_array = reverseArray(original_array)
print(reversed_array)  # Output: [5, 4, 3, 2, 1]


#Notes

""" ```python
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
    ```


This line uses a `for` loop to iterate through the indices of the array in reverse order. Let's dissect the components:

- LENGTH `len(arr) - 1`: This part finds the index of the last element in the input array (`arr`). In Python, arrays are zero-indexed, so `len(arr)` gives the total number of elements in the array. Since indexing starts from 0, `len(arr) - 1` represents the index of the last element in the array.

- STOP `-1`: This is the stopping condition for the loop. It signifies that the loop will continue until it reaches the index `-1` (exclusive).

- STEP `-1`: This is the step or increment value for the loop. It means the loop will iterate backward by reducing the index by 1 in each iteration.

Now, let's put it all together:

The `for` loop runs through the array indices in reverse order, starting from the index of the last element (`len(arr) - 1`) and ending at `-1`, decreasing by `-1` in each step. Inside the loop:

- `i` represents the current index being accessed.
- `arr[i]` accesses the element at index `i` in the input array `arr`.
- `reversed_arr.append(arr[i])` appends the element at index `i` to the `reversed_arr` list, effectively reversing the elements from the original array into the new reversed array.

 """
