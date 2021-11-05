
# sub_array = [2, 4, 5, 6, 33, 3, 1, 2, 9]

# for i, val in enumerate(sub_array):
#     print(i, val)

def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    start = 0
    curr_sum = 0
    for end, val in enumerate(arr):
        curr_sum += val
        pos = end - start + 1
        if pos == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
    return max_sum


arr = [2, 3, 4, 1, 5]
k = 3
print("actual", max_sum_subarray(arr, k))
