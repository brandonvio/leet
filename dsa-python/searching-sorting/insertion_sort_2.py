def insertion_sort(arr):
    for i in range(len(arr)):
        current_value = arr[i]
        j = i
        while j > 0 and arr[j - 1] > current_value:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = current_value

    return arr


print(insertion_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
# arr1, expected_result = [3, 2, 1, 9, 4, 6, 5, 8, 7, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(arr1, expected_result)
# result = insertion_sort(arr1)
# print(result)
# assert result == expected_result

# arr1, expected_result = [5, 2, 1, 3], [1, 2, 3, 5]
# print(arr1, expected_result)
# result = insertion_sort(arr1)
# print(result)
# assert result == expected_result
