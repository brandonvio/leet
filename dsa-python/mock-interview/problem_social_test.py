from typing import List
from collections import defaultdict


def test_problem_social_0():
    def remove_dup(s: str) -> str:
        tracker = set()
        new_s = []
        for char in s:
            if char not in tracker:
                new_s.append(char)
                tracker.add(char)

        return ''.join(new_s)

    result = remove_dup("tree traversal")
    print(result)
    assert result == "tre avsl"


def test_problem_social_1():
    """
    Problem¶
    Given a list of integers and a target number, write a function that returns a boolean indicating if its possible to sum two integers from the list to reach the target number

    Requirements
    Try pen/paper before coding out your solution

    You can not use an integer element twice. Optimize for time over space
    """

    def can_sum(nums: List[int], target: int) -> bool:
        tracker = set()

        for num in nums:
            num2 = target - num
            if num2 in tracker:
                return True
            tracker.add(num)

        return False

    result = can_sum([1, 2, 3], 5)
    assert result == True
    # print(result)
    result = can_sum([4, 1, 2, 3], 6)
    assert result == True
    # print(result)
    result = can_sum([1, 2, 3], 7)
    assert result == False
    # print(result)


def test_problem_social_2():
    """
    Problem
    Given a list of account ID numbers (integers) which contains duplicates , find the one unique integer. (the list is guaranteed to only have one unique (non-duplicated) integer

    Requirements
    Do not use built-in Python functions or methods
    """

    def find_unique(nums: List[int]) -> int:
        tracker = defaultdict(int)
        for num in nums:
            tracker[num] += 1

        for key in tracker.keys():
            if tracker[key] == 1:
                return key

        return None

    result = find_unique([1, 1, 3, 7, 3, 3, 4, 4])
    print(result)
    assert result == 7


# def test_problem_social_2_xor():
#     """
#     Problem
#     Given a list of account ID numbers (integers) which contains duplicates , find the one unique integer. (the list is guaranteed to only have one unique (non-duplicated) integer
#
#     Requirements
#     Do not use built-in Python functions or methods
#     """
#
#     def find_unique(nums: List[int]) -> int:
#         unique_id = 0
#
#         for i in nums:
#             unique_id ^= i
#
#         return unique_id
#
#     result = find_unique([1, 1, 3, 7, 3, 3, 4, 4])
#     print(result)
#     assert result == 7


def test_problem_social_3():
    """
    Problem¶
    Create a function that takes in a list of unsorted prices (integers) and a maximum possible price value, and return a sorted list of prices

    Requirements
    Your function should be able to perform this in less than O(nlogn) time.
    """

    def sort(prices: List[int], max_price: int) -> List[int]:
        prices_to_counts = [0] * (max_price + 1)

        for price in prices:
            prices_to_counts[price] += 1

        sorted_prices = []
        for price, count in enumerate(prices_to_counts):
            for time in range(count):
                sorted_prices.append(price)

        return sorted_prices


"""
"""
