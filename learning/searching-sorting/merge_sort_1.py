from typing import List


def merge_sort(arr: List[int]):
    arr_len = len(arr)
    if arr_len > 1:
        left_arr = arr[:arr_len // 2]
        right_arr = arr[arr_len // 2:]

        print("left:", left_arr)
        print("right:", right_arr)

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr


arr_test = [3, 2, 1]
print(merge_sort(arr_test))
