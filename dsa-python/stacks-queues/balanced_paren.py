"""
Determine if parens are balanced.
"""
def balanced_paren(s):
    if len(s) == 1:
        return False

    if len(s) % 2 != 0:
        return False

    open_chars = set(["{", "(", "["])
    pairs = set([ ("{","}") , ("(",")"), ("[","]") ])

    _stack = []
    for char in s:
        if char in open_chars:
            _stack.append(char)
        else:
            if len(_stack) == 0: # if empty return false
                return False
            open_char = _stack.pop() # get next char on stack
            if (open_char, char) not in pairs:
                return False

    return len(_stack) == 0


test_val, expected_result = "[]", True
print(test_val, expected_result)
assert balanced_paren(test_val) == expected_result

test_val, expected_result = ")))[]", False
print(test_val, expected_result)
assert balanced_paren(test_val) == expected_result

test_val, expected_result = "[", False
print(test_val, expected_result)
assert balanced_paren(test_val) == expected_result

test_val, expected_result = "[[[", False
print(test_val, expected_result)
assert balanced_paren(test_val) == expected_result

test_val, expected_result = "((()))[[{{}}]]", True
print(test_val, expected_result)
assert balanced_paren(test_val) == expected_result

test_val, expected_result = "((()))[[{{}}]", False
print(test_val, expected_result)
assert balanced_paren(test_val) == expected_result
