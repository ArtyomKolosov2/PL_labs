# Программа находит сумму элементов списка
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.3.2020
def sum_of_elements_rec(nums):
    if not (isinstance(nums, list) and nums):
        return 0
    return nums.pop(len(nums) - 1) + sum_of_elements_rec(nums)


def sum_of_elements_iter(nums):
    if not (isinstance(nums, list) and  nums):
        return None
    summa = 0
    
    for num in nums:
        summa += num
    return summa

n = [1,2,3]
print(n)
print("Sum of numbers = {0}".format(sum_of_elements_rec(n[:])))
print("Iteration way".center(25, "-"))
print("Sum of numbers = {0}".format(sum_of_elements_iter(n)))
input()
