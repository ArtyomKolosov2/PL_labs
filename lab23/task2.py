# Программа находит сумму всех чисел
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.3.2020


def sum_of_num_recursion(number):
    if number == 0:
        return 0
    summa = number % 10
    return summa + sum_of_num_recursion(number // 10)


def sum_of_num_iter(number):
    if number == 0:
        return 0
    summa = 0
    while number:
        summa += number % 10
        number //= 10
    return summa

n = 123
print("Sum of numbers {0} = {1}".format(n, sum_of_num_recursion(n)))
print("Iteration way".center(25, "-"))
print("Sum of numbers {0} = {1}".format(n, sum_of_num_iter(n)))
input("Press Enter")
