from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


sol = Solution()
#
m = 7
nums1 = [2, 3, 10, 13, 15, 16, 17, 0, 0, 0]
n = 3
nums2 = [1, 12, 22]
print(nums1)
sol.merge(nums1, m, nums2, n)
print(nums1)
assert nums1 == [1, 2, 3, 10, 12, 13, 15, 16, 17, 22]

m = 3
nums1 = [1, 12, 22, 0, 0, 0, 0, 0, 0, 0]
n = 7
nums2 = [2, 3, 10, 13, 15, 16, 17]
print(nums1)
sol.merge(nums1, m, nums2, n)
print(nums1)
assert nums1 == [1, 2, 3, 10, 12, 13, 15, 16, 17, 22]

# nums1 = [2, 3, 0]
# m = 2
# nums2 = [1]
# n = 1
# sol.merge(nums1, m, nums2, n)

# nums1 = [2, 3, 0]
# m = 2
# nums2 = [1]
# n = 1
# sol.merge(nums1, m, nums2, n)

# nums1 = [4, 5, 6, 0, 0, 0]
# m = 3
# nums2 = [1, 2, 3]
# n = 3
# sol.merge(nums1, m, nums2, n)
#
# #
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# sol.merge(nums1, m, nums2, n)
#
# nums1 = [1, 0, 0]
# m = 1
# nums2 = [2, 3]
# n = 2
# sol.merge(nums1, m, nums2, n)

# nums1 = [3, 0, 0]
# m = 1
# nums2 = [1, 2]
# n = 2
# sol.merge(nums1, m, nums2, n)
