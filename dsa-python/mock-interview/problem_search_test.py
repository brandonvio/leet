
def test_phone_screen():
    def fib(n: int) -> int:
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    result = fib(10)
    # print(result)
    assert result == 55


"""
Question¶
Given a dice which rolls 1 to 7 (with uniform probability), simulate a 5 sided dice. Preferably, write your solution as a function.

Requirements
You MUST do this on pen and paper or on a whiteboard. No actual coding is allowed until you've solved it on pen and paper!
"""
def test_problem_search_1():
    pass

"""
Question¶
Given a dice which rolls from 1 to 5, simulate a uniform 7 sided dice!

Requirements
You MUST do this on pen and paper or on a whiteboard. No actual coding is allowed until you've come up with a solution by hand!
"""
def test_problem_search_2():
    pass

"""
Question
Given a string, write a function that uses recursion to reverse it.

Requirements
You MUST use pen and paper or a whiteboard to answer this, no coding allowed!
"""
def test_problem_search_3():
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


"""
Question
Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4.

Requirements
Feel free to code this out (but its recommended that you use paper/pencil or whiteboard)
"""
def test_problem_search_4():
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
    print(result)

    result = find_square(15)
    print(result)

    result = find_square(17)
    print(result)

    result = find_square(110)
    print(result)

    result = find_square(110000111000)
    print(result)

















"""
"""
