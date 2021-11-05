"""
test if string is unique
"""


def is_unique(s: str) -> bool:
    s_set = set()
    for v in s:
        if v in s_set:
            return False
        else:
            s_set.add(v)
    return True


print(is_unique("AAAAaaaBBBBB"))
print(is_unique("abcd1234"))
