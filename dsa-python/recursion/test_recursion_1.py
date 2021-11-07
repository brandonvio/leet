from typing import List


def test_recursion_fact():
    def fact(n):
        # base case
        if n == 0:
            return 1

        # recursive case
        else:
            val_left = n
            val_right = fact(n - 1)
            result_fact = val_left * val_right
            return result_fact

    result = fact(4)
    assert result == 24

    result = fact(5)
    assert result == 120


def test_recursion_sum():
    def rec_sum(n):
        # base case
        if n == 0:
            return 0

        # recursive case
        else:
            right_sum = rec_sum(n - 1)
            result_sum = n + right_sum
            return result_sum

    result = rec_sum(4)
    assert result == 10


def test_recursion_sum2():
    def rec_sum(s: str) -> int:
        # base case
        if len(s) == 0:
            return 0

        # recursive case
        else:
            val_left = int(s) % 10
            s_new = s[0:len(s) - 1]
            val_right = rec_sum(s_new)
            val = val_left + val_right
            return val

    result = rec_sum("4321")
    assert result == 10


def test_reverse_string():
    def reverse(s: str):
        # base case
        if s == "":
            return ""

        # recursive case
        else:
            end_index = len(s) - 1
            val_left = s[end_index]
            s_new = s[0:end_index]
            val_right = reverse(s_new)
            return val_left + val_right

    result = reverse("abcdef")
    assert result == "fedcba"


def test_permute_string():
    def permute(s: str):
        out = []
        # base case
        if len(s) == 1:
            out = [s]

        # recursive case
        else:
            for i, let in enumerate(s):
                for perm in permute(s[:i] + s[i + 1:]):
                    out += [let + perm]
                    pass
        return out

    result = permute("abc")
    assert result == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


def test_fibonacci_memo():
    def fib(n: int, memo=None):
        if memo is None:
            memo = {}
        # base case
        if n < 2:
            return n

        # recursive case
        else:
            if n in memo:
                return memo[n]
            else:
                val_left = fib(n - 1, memo)
                val_right = fib(n - 2, memo)
                memo[n] = val_left + val_right
                return memo[n]

    result = fib(10)
    assert result == 55
    assert fib(1) == 1
    assert fib(12) == 144
    assert fib(23) == 28657


def test_fibonacci():
    def fib(n: int):
        # base case
        if n < 2:
            return n

        # recursive case
        else:
            val_left = fib(n - 1)
            val_right = fib(n - 2)
            return val_left + val_right

    result = fib(10)
    assert result == 55
    assert fib(1) == 1
    assert fib(23) == 28657


def test_fibonacci_iter():
    def fib(n: int):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    result = fib(10)
    assert result == 55
    assert fib(1) == 1
    assert fib(23) == 28657


def test_coin_change_recur():
    def coin_change(target: int, coins: List[int]):
        min_coins = target
        if target in coins:
            return 1
        else:
            for i in [c for c in coins if c <= target]:
                num_coins = 1 + coin_change(target - i, coins)
                if num_coins < min_coins:
                    min_coins = num_coins
        return min_coins

    result = coin_change(12, [1, 5, 10])
    assert result == 3


def test_coin_change_memo():
    def coin_change(target: int, coins: List[int], known_results: List[int]):
        min_coins = target

        if target in coins:
            known_results[target] = 1
            return 1

        elif known_results[target] > 0:
            return known_results[target]

        else:
            for i in [c for c in coins if c <= target]:
                num_coins = 1 + coin_change(target - i, coins, known_results)
                if num_coins < min_coins:
                    min_coins = num_coins
                    known_results[target] = min_coins

        return min_coins

    result = coin_change(74, [1, 5, 10, 25], [0] * 75)
    assert result == 8
