import random

nums = [7, 6, 5, 4, 3, 2, 1, 0]


def quick_select(left, right, k):
    if left == right:
        return
    pivot_index = random.randint(left, right)
    i, j = left, right
    while True:
        while nums[i] < nums[pivot_index]:
            i += 1
        while nums[j] > nums[pivot_index]:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]

    if left < i - 1:
        quick_select(left, i - 1, k)
    if right > i + 1:
        quick_select(i + 1, right, k)
    return nums[k - 1]


quick_select(0, len(nums) - 1, 1)
