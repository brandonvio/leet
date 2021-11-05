"""
Sequential search
"""


def seq_search(arr, ele):
    for val in arr:
        if val == ele:
            return True
        else:
            pass
    return False


def seq_search_ww(arr, ele):
    ind = 0
    found = False

    while ind < len(arr) and not found:
        if arr[ind] == ele:
            found = True
        else:
            ind += 1

    return found


arr, val, expected_result = [1, 2, 4, 6, 7, 10], 11, False
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 1, True
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 10, True
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 4, True
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 0, False
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

# ww
arr, val, expected_result = [1, 2, 4, 6, 7, 10], 11, False
print(arr, val, expected_result)
assert seq_search_ww(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 1, True
print(arr, val, expected_result)
assert seq_search_ww(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 10, True
print(arr, val, expected_result)
assert seq_search_ww(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 4, True
print(arr, val, expected_result)
assert seq_search_ww(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 0, False
print(arr, val, expected_result)
assert seq_search_ww(arr, val) == expected_result
