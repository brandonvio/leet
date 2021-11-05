"""
find the missing number:
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
5 is missing
"""
from collections import defaultdict
from typing import List


def find_missing_1(arr1: List[int], arr2: List[int]):
    tracker = set()
    for val in arr1:
        tracker.add(val)

    for val in arr2:
        tracker.remove(val)

    return tracker.pop()


def find_missing_2(arr1: List[int], arr2: List[int]):
    d = defaultdict(int)
    for val in arr2:
        d[val] += 1

    for val in arr1:
        if d[val] == 0:
            return val
        else:
            d[val] -= 1


print(find_missing_2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
