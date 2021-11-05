"""
Sequential search with sorted array
"""

def seq_search(arr, ele):
    for val in arr:
        print(val)
        if val == ele:
            return True
    return False

def seq_search_sorted(arr, ele):
    for val in arr:
        print(val)
        if val == ele:
            return True
        else:
            if val > ele:
                return False
    return False


def seq_search_ww(arr, ele):
    ind = 0
    found = False

    while ind < len(arr) and not found:
        print(arr[ind])
        if arr[ind] == ele:
            found = True
        else:
            if arr[ind] > ele:
                found = False
                break
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

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 3, False
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 3, False
print(arr, val, expected_result)
assert seq_search_sorted(arr, val) == expected_result

arr, val, expected_result = [1, 2, 4, 6, 7, 10], 0, False
print(arr, val, expected_result)
assert seq_search(arr, val) == expected_result

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
