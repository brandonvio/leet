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
from typing import List
import sys

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


prices = [12,11,15,3,10]
profit = solution(prices)
assert profit == 7
print(profit)
