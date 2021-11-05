"""
find the largest continuous sum
"""
from typing import List


def large_cont_sum_1(arr1: List[int]):
    if len(arr1) == 0:
        return None
    max_sum = 0
    max_idx = (0, 0)
    for i in range(len(arr1)):
        j = i + 1
        while j < len(arr1):
            curr_max_sum = max_sum
            max_sum = max(max_sum, sum(arr1[i:j + 1]))
            if max_sum > curr_max_sum:
                max_idx = (i, j)
            j += 1
    return max_sum, max_idx


print(large_cont_sum_1([1, 2, -1, 3, 4, 10, 10, -10, -1]))


def large_cont_sum_2(arr1: List[int]):
    if len(arr1) == 0:
        return None

    max_sum = current_sum = 0

    for num in arr1:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


print(large_cont_sum_1([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_cont_sum_2([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_cont_sum_2([-1, 1]))
print(large_cont_sum_2([1, 2, -1, 3, 4, -1]))
