# Программа проверяет возможность сущ. степени
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.3.2020


def check_power_recursion(num, n):
    if num == n or n == 1:
        return 1
    if num < n:
        return 0

    return check_power_recursion(num / n, n)


def check_power_iter(num, n):
    result = 0
    for i in range(num, 0, -n):
        if i == n:
            result = 1
            break
    return result

num = 8
n = 2
if check_power_recursion(num, n):
    print("{0} - is a power of {1}".format(num, n))
print("Iteration way".center(25, "-"))
if check_power_iter(num, 4):
    print("{0} - is a power of {1}".format(num, n))
input("Press Enter")
