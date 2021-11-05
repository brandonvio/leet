class Solution:
    def length_of_longest_substring_1(self, t_str: str) -> int:
        b_pointer = 0
        a_pointer = 0
        t_max = 0
        t_list = []

        while b_pointer < len(t_str):
            t_char = t_str[b_pointer]
            if t_char in t_list:
                t_list.remove(t_str[a_pointer])
                a_pointer += 1
            else:
                t_list.append(t_char)
                b_pointer += 1
                t_max = max(t_max, len(t_list))

        return t_max

    def length_of_longest_substring_2(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        s_len = len(s)
        for r in range(s_len):
            s_r = s[r]
            while s_r in char_set:
                s_l = s[l]
                char_set.remove(s_l)
                l += 1
            char_set.add(s_r)
            r_l = r - l + 1
            res = max(res, r_l)
        return res

    def length_of_longest_substring_3(self, s):
        chars = set()
        m = 0
        l = 0
        for v in s:
            while v in chars:
                chars.remove(s[l])
                l += 1
            chars.add(v)
            m = max(m, len(chars))

        return m
