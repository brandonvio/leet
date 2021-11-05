class Solution:
    def get_longest_non_repeat(self, s):
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


sol = Solution()
print(sol.get_longest_non_repeat("pwwkew"))
print(sol.get_longest_non_repeat("abccccddddddee"))
