from longest_non_repeat import Solution


def test_find_missing_1():
    sol = Solution()
    t_ans = sol.length_of_longest_substring_1("aab")
    assert t_ans == 2

    t_ans = sol.length_of_longest_substring_1("dvdf")
    assert t_ans == 3

    t_ans = sol.length_of_longest_substring_2("pwwkew")
    assert t_ans == 3

    t_ans = sol.length_of_longest_substring_3("bbbbb")
    assert t_ans == 1
