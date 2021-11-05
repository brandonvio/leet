def binary_search(arr, ele):
    if len(arr) == 0:
        return False

    mid = round(len(arr) / 2)
    if ele == arr[mid]:
        return True

    if ele > arr[mid]:
        return binary_search(arr[mid + 1:], ele)
    else:
        return binary_search(arr[:mid], ele)


# _range = range(0, 100)
# arr, val, expected_result = _range, -1, False
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4], 3, False
print(arr, val, expected_result)
assert binary_search(arr, val) == expected_result

# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 10, True
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 4, True
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 3, False
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 3, False
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 0, False
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 11, False
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 1, True
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 10, True
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 4, True
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
#
# arr, val, expected_result = [1, 2, 4, 6, 7, 10], 0, False
# print(arr, val, expected_result)
# assert binary_search(arr, val) == expected_result
