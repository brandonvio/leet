from typing import List


def test_ride_search_1():
    """
    Problem
    Given a list of integers, find the largest product you could make from 3 integers in the list

    Requirements
    You can assume that the list will always have at least 3 integers

    Paper/pencil only, don't code this out until you've solved it as far as you can by hand.
    """

    def find_highest_of_3(lst):
        high = max(lst[0], lst[1])
        low = min(lst[0], lst[1])
        high_prod2 = lst[0] * lst[1]
        low_prod2 = lst[0] * lst[1]
        high_prod3 = lst[0] * lst[1] * lst[2]

        for num in lst[2:]:
            high_prod3 = max(high_prod3, num * high_prod2, num*low_prod2)
            high_prod2 = max(high_prod2, num * high, num * low)
            low_prod2 = min(high_prod2, num * high, num * low)
            high = max(high, num)
            low = min(low, num)

        return high_prod3

    result = find_highest_of_3([2, 3, 3, 1, 0, -5, -5, 3, 2, 1])
    print(result)



def test_ride_search_2():
    """
    Problem
    Write a function that given a target amount of money and a list of possible coin denominations, returns the number of ways to make change for the target amount using the coin denominations

    Requirements
    Write out your work on paper/pencil, then see if you can code up your solution
    https://stackoverflow.com/questions/14992411/understanding-change-making-algorithm
    https://en.wikipedia.org/wiki/Change-making_problem
    https://www.youtube.com/watch?v=DJ4a7cmjZY0
    """
    def list_possible(n: int, coins: List[int]) -> int:
        arr = [1] + [0] * n

        for coin in coins:
            for i in range(coin, n + 1):
                arr[i] += arr[i - coin]

        if n == 0:
            return 0
        else:
            return arr[n]

    result = list_possible(100, [1, 2, 3])
    print(result)


def test_ride_search_3():
    """
    Problem
    Given a binary tree, check whether it’s a binary search tree or not.

    Requirements
    Use paper/pencil, do not code this in an IDE until you've done it manually

    Do not use built-in Python libraries to do this, but do mention them if you know about them
    """
    INFINITY = float('infinity')
    NEG_INFINITY = float('-infinity')

    class Node:
        def __init__(self, val=None):
            self.left = None
            self.right = None
            self.val = val


    def is_bst(tree, min_val=NEG_INFINITY, max_val=INFINITY):
        if tree is None:
            return True

        if not min_val <= tree.val <= max_val:
            return False

        return is_bst(tree.left, min_val, tree.val) and is_bst(tree.right, tree.val, max_val)


    def is_bst_2(tree, last_node=[NEG_INFINITY]):
        if tree is None:
            return True

        if not is_bst_2(tree.left, last_node):
            return False

        if tree.val < last_node[0]:
            return False

        last_node[0] = tree.val

        return is_best_2(tree.right, last_node)


"""
"""
