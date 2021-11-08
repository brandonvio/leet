from typing import List
import sys


def test_problem_ec_1():
    """
    Problem
    You've been given a list of historical stock prices for a single day for Amazon stock. The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock, the element at index 1 is the next recorded price of the stock for that day, etc. Your task is to write a function that will return the maximum profit possible from the purchase and sale of a single share of Amazon stock on that day. Keep in mind to try to make this as efficient as possible.

    For example, if you were given the list of stock prices:

    prices = [12,11,15,3,10]

    Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).

    Requirements
    Try to solve this problem with paper/pencil first without using an IDE. Also keep in mind you should be able to come up with a better solution than just brute forcing every possible sale combination

    Also you can't "short" a stock, you must buy before you sell the stock.

    Good Luck!¶
    """

    def solution(price_list: List[int]) -> int:
        min_price: int = sys.maxsize
        min_index: int = 0
        max_price: int = 0

        for i, current_price in enumerate(price_list):
            if current_price < min_price:
                min_price = current_price
                min_index = i

        for i, current_price in enumerate(price_list):
            if current_price > max_price and i > min_index:
                max_price = current_price

        return max_price - min_price

    prices = [12, 11, 15, 3, 10]
    profit = solution(prices)
    assert profit == 7


def test_problem_ec_1_correct():
    """
    This is the correct solution. My solution isn't bad. It is still basically linear.
    But this one is more correct.
    """

    def solution(price_list: List[int]) -> int:
        if len(price_list) < 2:
            return None

        min_price = price_list[0]
        max_profit = 0

        for price in price_list:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)

        return max_profit

    prices = [12, 11, 15, 3, 10]
    profit = solution(prices)
    assert profit == 7


def test_problem_ec_2():
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

    result = solution([1, 2, 3, 4])
    assert result == [24, 12, 8, 6]


def test_problem_ec_2_correct():
    """
    This is a brute force solution n^2 time. Working on solution for better time.
    """

    def solution(arr: List[int]) -> List[int]:
        output_list = [None] * len(arr)

        product = 1
        i = 0
        while i < len(arr):
            output_list[i] = product
            product *= arr[i]
            i += 1

        product = 1
        i = len(arr) - 1
        while i >= 0:
            output_list[i] *= product
            product *= arr[i]
            i -= 1

        return output_list

    result = solution([1, 2, 3, 4])
    assert result == [24, 12, 8, 6]


def test_problem_ec_3():
    """
    Problem
    Given two rectangles, determine if they overlap. The rectangles are defined as a Dictionary, for example:

    In [2]:
    r1 = {

             # x and y coordinates of the bottom-left corner of the rectangle
             'x': 2 , 'y': 4,

             # Width and Height of rectangle
             'w':5,'h':12}
    If the rectangles do overlap, return the dictionary which describes the overlapping section

    Requirements
    Make sure the dictionary you output is in the same form as the input.

    Feel free to use an IDE for the code, but make sure you use paper/pencil or whiteboard to draw out your plan and logic
    """

    def solution(r1, r2):
        r3 = None

        # check bottom left corner of r2 against r1
        if r2["x"] < r1["x"] + r1["w"] and r2["y"] < r1["y"] + r1["h"]:
            r3 = {
                "x": r2["x"],
                "y": r2["y"],
                "w": (r1["x"] + r1["w"]) - r2["x"],
                "h": (r1["y"] + r1["h"]) - r2["y"]
            }

        # check top left corner of r2 against r1

        # check top right corner of r2 against r1

        # check top bottom corner of r2 against r1

        # done
        return r3

    r1 = {
        # x and y coordinates of the bottom-left corner of the rectangle
        'x': 2, 'y': 4,
        # Width and Height of rectangle
        'w': 5, 'h': 12
    }

    r2 = {
        # x and y coordinates of the bottom-left corner of the rectangle
        'x': 5, 'y': 14,
        # Width and Height of rectangle
        'w': 5, 'h': 6
    }

    result = solution(r1, r2)
    assert result["x"] == 5
    assert result["y"] == 14
    assert result["w"] == 2
    assert result["h"] == 2


def test_problem_ec_3_correct():
    def calc_overlap(coor1: int, dim1: int, coor2: int, dim2: int) -> ():
        greater = max(coor1, coor2)
        lower = min(coor1 + dim1, coor2 + dim2)
        if greater >= lower:
            return None, None
        overlap = lower - greater
        return greater, overlap

    def calc_rect_overlap(r1, r2):
        x_overlap, w_overlap = calc_overlap(r1['x'], r1['w'], r2['x'], r2['w'])
        y_overlap, h_overlap = calc_overlap(r1['y'], r1['h'], r2['y'], r2['h'])

        if not w_overlap or not h_overlap:
            return None

        return {
            'x': x_overlap,
            'y': y_overlap,
            'w': w_overlap,
            'h': h_overlap
        }

    r1 = {
        # x and y coordinates of the bottom-left corner of the rectangle
        'x': 2, 'y': 4,
        # Width and Height of rectangle
        'w': 5, 'h': 12
    }

    r2 = {
        # x and y coordinates of the bottom-left corner of the rectangle
        'x': 5, 'y': 14,
        # Width and Height of rectangle
        'w': 5, 'h': 6
    }

    result = calc_rect_overlap(r1, r2)
    assert result["x"] == 5
    assert result["y"] == 14
    assert result["w"] == 2
    assert result["h"] == 2
