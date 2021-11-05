from find_missing_number import find_missing_1, find_missing_2


# content of test_sample.py
def test_find_missing_1():
    missing_num = find_missing_1([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
    assert missing_num == 5


def test_find_missing_2():
    missing_num = find_missing_2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
    assert missing_num == 5


def test_find_missing_3():
    missing_num = find_missing_2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
    assert missing_num == 5
