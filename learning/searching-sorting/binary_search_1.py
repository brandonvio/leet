count = 0

def binary_search(arr, ele):
    global count
    count += 1
    if len(arr) == 0:
        return False

    mid = round(len(arr) / 2)

    if ele == arr[mid]:
        print("found", ele, arr[mid])
        return True
    elif ele > arr[mid]:
        return binary_search(arr[mid + 1:], ele)
    else:
        return binary_search(arr[:mid], ele)


print(count)
_range = range(0, 100)
arr, val, expected_result = _range, -1, False
print(arr, val, expected_result)
assert binary_search(arr, val) == expected_result
print(count)


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
