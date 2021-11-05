# #sliddingwindow

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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


sol = Solution()
# t_ans = sol.lengthOfLongestSubstring("aab")
# print(t_ans)

# t_ans = sol.lengthOfLongestSubstring("dvdf")
# print(t_ans)

t_ans = sol.lengthOfLongestSubstring("acbbacbb")
print(t_ans)

# "pwwkew"

# t_ans = sol.lengthOfLongestSubstring("bbbbb")
# print(t_ans)
x1 = {}
x2 = []
x3 = set()

x2.append()
x3.add(1)
