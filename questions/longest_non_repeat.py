class Solution:
    def lengthOfLongestSubstring(self, t_str: str) -> int:
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


sol = Solution()
# t_ans = sol.lengthOfLongestSubstring("aab")
# print(t_ans)

# t_ans = sol.lengthOfLongestSubstring("dvdf")
# print(t_ans)

t_ans = sol.lengthOfLongestSubstring("pwwkew")
print(t_ans)

# "pwwkew"

# t_ans = sol.lengthOfLongestSubstring("bbbbb")
# print(t_ans)
