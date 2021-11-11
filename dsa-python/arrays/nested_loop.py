# https://www.youtube.com/watch?v=9qPtxAY9bKA

def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                counter += 1
    return counter


n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
# ar = [1, 3, 2]
print(divisibleSumPairs(n, k, ar))

# https://www.youtube.com/watch?v=9qPtxAY9bKA
# from collections import defaultdict
#
#
# def divisibleSumPairs(n, k, ar):
#     counter, tracker = 0, defaultdict(int)
#     for val in ar:
#         m = val % k
#         compl = k - m if k - m != k else 0
#         if compl in tracker:
#             counter += tracker[compl]
#         tracker[m] += 1
#     return counter
#
#
# n = 3
# k = 3
# ar = [1, 3, 2, 6, 1, 2]
# # ar = [1, 3, 2]
# print(divisibleSumPairs(n, k, ar))
