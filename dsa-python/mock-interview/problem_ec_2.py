"""
Problem
Given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers except for the element at that index

For example, an input of [1,2,3,4] would return [24,12,8,6] by performing [2×3×4,1×3×4,1×2×4,1×2×3]

Requirements
You can not use division in your answer! Meaning you can't simply multiply all the numbers and then divide by eahc element for each index!

Try to do this on a white board or with paper/pencil.
"""
from typing import List

"""
This is a brute force solution n^2 time. Working on solution for better time.
"""
def solution(arr: List[int]) -> List[int]:

    def multiply_nums(nums: List[int]) -> int:
        multiplied_num = 1
        for num in nums:
            multiplied_num = multiplied_num * num
        return multiplied_num

    return_list = []
    for i in range(len(arr)):
        new_arr = list(arr)
        del new_arr[i]
        val = multiply_nums(new_arr)
        return_list.append(val)

    return return_list

print("solution([1,2,3,4]):")
result = solution([1,2,3,4])
print(result)
assert result == [24,12,8,6]
