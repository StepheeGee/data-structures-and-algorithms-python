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


