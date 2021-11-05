


def bubble_sort(arr):
    for i in range(0, len(arr) -1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp_j = arr[j]
                arr[j] = arr[i]
                arr[i] = temp_j
    return arr



arr1, expected_result = [3, 2, 1, 9, 4, 6, 5, 8, 7, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr1, expected_result)
result = bubble_sort(arr1)
print(result)
assert result  == expected_result


arr1, expected_result = [100, -1, 0], [-1, 0, 100]
print(arr1, expected_result)
result = bubble_sort(arr1)
print(result)
assert result  == expected_result
