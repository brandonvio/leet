from typing import List

from nose.tools import assert_equal


def pair_sum_count(arr: List[int], t: int):
    n = len(arr)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            print(arr[i], arr[j])
            if arr[i] + arr[j] == t:
                c += 1
    return c


# print(pair_sum_count([1, 3, 2, 2, 4, 0], 4))


def pair_sum_count_best(arr: List[int], target_num: int):
    nums = set()
    c = 0
    for v in arr:
        k = target_num - v
        if k in nums:
            c += 1
        else:
            nums.add(v)
    return c


# print(pair_sum_count_best([1, 3, 2, 2, 4, 0], 4))
assert_equal(pair_sum_count_best([1, 2, 3, 1], 3), 1)
# assert_equal(pair_sum_count_best([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
