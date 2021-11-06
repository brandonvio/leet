class Solution:
    def getLongestNonRepeat(self, s):
        l = 0
        v_max = 0
        char_set = set()

        for end, val in enumerate(s):
            while val in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(val)
            v_max = max(v_max, len(char_set))

        return v_max


sol = Solution()
# result = sol.getLongestNonRepeat("pwwkew")
result = sol.getLongestNonRepeat("abccccddddddee")
print(result)
