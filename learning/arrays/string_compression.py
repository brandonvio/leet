"""
string compression
"""
from collections import OrderedDict


def compress(s: str) -> str:
    s_dict = OrderedDict()
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1

    s_compress = ""
    for d in s_dict:
        s_compress += d + str(s_dict[d])

    return s_compress


print(compress("AAAAaaaBBBBB"))
