from typing import List


def merge_two_sorted(arr1: List[int], arr2: List[int]):
    new_arr = [0] * (len(arr1) + len(arr2))
    ind_1, ind_2, new_ind = len(arr1) - 1, len(arr2) - 1, len(new_arr) - 1
    while ind_1 >= 0 and ind_2 >= 0:
        if arr1[ind_1] > arr2[ind_2]:
            new_arr[new_ind] = arr1[ind_1]
            ind_1 -= 1
        else:
            new_arr[new_ind] = arr2[ind_2]
            ind_2 -= 1
        new_ind -= 1

    # while ind_1 >= 0:
    #     new_arr[new_ind] = arr1[ind_1]
    #     ind_1 -= 1
    #     new_ind -= 1

    while ind_2 >= 0:
        new_arr[new_ind] = arr2[ind_2]
        ind_2 -= 1
        new_ind -= 1

    return new_arr


arr2 = [2, 5, 7, 21, 22, 100, 104]
arr1 = [1, 15, 23]
sorted1 = merge_two_sorted(arr1, arr2)
expected = [1, 2, 5, 7, 15, 21, 22, 23, 100, 104]
assert sorted1 == expected
print(sorted1)

# arr3 = [3, 6, 8]
# sorted2 = merge_two_sorted(arr3, sorted1)
# expected = [1, 2, 3, 5, 6, 7, 8, 15, 21, 22, 23, 100, 104]
# assert sorted2 == expected
# print(sorted2)
#
# #
# arr4 = [4, 25, 101, 1000]
# sorted3 = merge_two_sorted(arr4, sorted2)
# expected = [1, 2, 3, 4, 5, 6, 7, 8, 15, 21, 22, 23, 25, 100, 101, 104, 1000]
# assert sorted3 == expected
# print(sorted3)
