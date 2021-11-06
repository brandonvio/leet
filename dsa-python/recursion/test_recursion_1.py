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
    print("")
    print("fact(4):" + str(result))
    assert result == 24

    result = fact(5)
    print("")
    print("fact(5):" + str(result))
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
    print("")
    print("rec_sum(4):" + str(result))


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
    print('reverse("abcdef"):' + result)


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
    # assert result == "fedcba"
    print('permute("abcd"):' + str(len(result)) + ", " + str(result))


def test_fibonacci_memo():
    def fib(n: int, cache=None):
        if cache is None:
            cache = {}
        # base case
        if n < 2:
            return n
        else:
            if n in cache:
                return cache[n]
            else:
                val_left = fib(n - 1, cache)
                val_right = fib(n - 2, cache)
                cache[n] = val_left + val_right
                return cache[n]

    result = fib(10)
    assert result == 55


def test_fibonacci():
    def fib(n: int):
        # base case
        if n < 2:
            return n
        else:
            val_left = fib(n - 1)
            val_right = fib(n - 2)
            return val_left + val_right

    result = fib(10)
    assert result == 55
