from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while (m > 0):
            i = m + n - 1
            if (nums1[m - 1] > nums2[n - 1]):
                print("m greater than n")
                print("move m to the end of the nums1 array.")
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                print("n greater than m")
                print("copy n to the end of the nums1 array.")
                nums1[i] = nums2[n - 1]
                print("decrement n by 1 to compare the previous number.")
                n -= 1

        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

        print(nums1)


sol = Solution()

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# sol.merge(nums1, m, nums2, n)

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
nums1 = [1, 0, 0]
m = 1
nums2 = [2, 3]
n = 2
sol.merge(nums1, m, nums2, n)

# nums1 = [3, 0, 0]
# m = 1
# nums2 = [1, 2]
# n = 2
# sol.merge(nums1, m, nums2, n)
