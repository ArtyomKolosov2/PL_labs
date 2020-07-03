# Программа разворачивает список
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.3.2020

def reverse_elements_recursion(nums):
    if not isinstance(nums, list) or not nums:
        return []
    return [nums[-1]] + reverse_elements_recursion(nums[:-1])


def reverse_elements_iter(nums):
    if not isinstance(nums, list) or not nums:
        return []
    for i in range(len(nums) // 2):
        nums[i], nums[-i - 1] = nums[-i - 1], nums[i]
    return nums


n = [1, 2, 3, 4]
print(reverse_elements_recursion(n))
print("Iteration way".center(25, "-"))
print(reverse_elements_iter(n))
input()
