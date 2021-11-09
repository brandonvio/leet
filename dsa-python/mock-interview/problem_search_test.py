def test_phone_screen():
    def fib(n: int) -> int:
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    result = fib(10)
    # print(result)
    assert result == 55


def test_fib_loop():
    def fib(n):
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a

    result = fib(10)
    # print(result)
    assert result == 55


def test_problem_search_1():
    from random import randint
    """
    Question¶
    Given a dice which rolls 1 to 7 (with uniform probability), simulate a 5 sided dice. Preferably, write your solution as a function.

    Requirements
    You MUST do this on pen and paper or on a whiteboard. No actual coding is allowed until you've solved it on pen and paper!
    """

    def dice7():
        return randint(1, 7)

    def convert7to5():
        roll = 7

        while roll > 5:
            roll = dice7()
        return roll

    result = convert7to5()
    # print("convert7to5()", str(result))
    assert result <= 5


def test_problem_search_2():
    """
    Question¶
    Given a dice which rolls from 1 to 5, simulate a uniform 7 sided dice!

    Requirements
    You MUST do this on pen and paper or on a whiteboard. No actual coding is allowed until you've come up with a solution by hand!
    """
    from random import randint

    def dice5():
        return randint(1, 5)

    def roll_dice():
        while True:
            roll_1 = dice5()
            roll_2 = dice5()
            num = ((roll_1 - 1) * 5) + (roll_2)
            # print("roll_1", roll_1, "roll_2", roll_2)
            # print("num", num)

            if num > 21:
                continue

            return num % 7 + 1

    for i in range(10):
        result = roll_dice()
        # print("roll_dice()", str(result))
        assert result <= 7


def test_problem_search_3():
    """
    Question
    Given a string, write a function that uses recursion to reverse it.

    Requirements
    You MUST use pen and paper or a whiteboard to answer this, no coding allowed!
    """

    def rev(s: str) -> str:
        if len(s) == 0:
            return ""

        else:
            left_val = s[len(s) - 1]
            right_val = rev(s[:len(s) - 1])
            return left_val + right_val

    result = rev("abc")
    # print(result)
    assert result == "cba"


def test_problem_search_3_correct():
    """
    Question
    Given a string, write a function that uses recursion to reverse it.

    Requirements
    You MUST use pen and paper or a whiteboard to answer this, no coding allowed!
    """

    def rev(s: str) -> str:
        if len(s) <= 1:
            return s

        else:
            left_val = rev(s[1:])
            right_val = s[0]
            return left_val + right_val

    result = rev("abcd")
    # print(result)
    assert result == "dcba"


def test_problem_search_4():
    """
    Question
    Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4.

    Requirements
    Feel free to code this out (but its recommended that you use paper/pencil or whiteboard)
    """

    def find_square(n: int) -> int:
        if n < 4:
            return None

        ans = None
        i = 2
        while ans is None:
            sq = i * i
            if sq == n:
                ans = i
            elif sq > n:
                ans = i - 1
            else:
                i += 1

        return ans

    result = find_square(9)
    # print(result)

    result = find_square(15)
    # print(result)

    result = find_square(17)
    # print(result)

    result = find_square(110)
    # print(result)

    result = find_square(110000111000)
    # print(result)


def test_problem_search_4_correct():
    """
    Question
    Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4.

    Requirements
    Feel free to code this out (but its recommended that you use paper/pencil or whiteboard)
    """

    def find_square(n: int) -> int:
        if n < 0:
            raise ValueError

        if n == 1:
            return 1

        low = 0
        high = (n / 2) + 1
        while low + 1 < high:
            mid = low + (high - low) / 2
            square = mid ** 2
            if square == n:
                return mid
            elif square < n:
                low = mid
            else:
                high = mid

        return round(low)

    result = find_square(9)
    assert result == 3

    result = find_square(16)
    assert result == 4
    # print(result)

    result = find_square(15)
    # print(result)

    result = find_square(17)
    # print(result)

    result = find_square(110)
    # print(result)

    result = find_square(110000111000)
    # print(result)


"""
"""
