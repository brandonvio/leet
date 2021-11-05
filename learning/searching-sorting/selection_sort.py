def selection_sort(arr):
    for i in range(len(arr) - 1):
        position_of_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[position_of_min]:
                position_of_min = j
        temp_i = arr[i]
        arr[i] = arr[position_of_min]
        arr[position_of_min] = temp_i
    return arr


# arr1, expected_result = [3, 2, 1, 9, 4, 6, 5, 8, 7, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(arr1, expected_result)
# result = selection_sort(arr1)
# print(result)
# assert result == expected_result

arr1, expected_result = [100, -1, 0], [-1, 0, 100]
print(arr1, expected_result)
result = selection_sort(arr1)
print(result)
assert result == expected_result
