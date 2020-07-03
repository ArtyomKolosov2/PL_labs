# Программа вычесляет x^n/n!
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.3.2020


def fact_recursion(n=0):
    if n == 0:
        return 1
    return n * fact_recursion(n - 1)


def fact_iter(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact


def pow_rec(x, n):
    if n == 0:
        return 1
    return x * pow_rec(x, n - 1)


def pow_iter(x, n):
    num = x
    for i in range(1, n):
        x *= num
    return x


def pow_fact_rec(x, n):
    return pow_rec(x, n) / fact_recursion(n)


def pow_fact_iter(x, n):
    return pow_iter(x, n) / fact_iter(n)

x = 2
n = 8
print("{0}^{1}/!{1} = {2}".format(x, n, pow_fact_rec(x, n)))
print("Iteration way".center(25, "-"))
print("{0}^{1}/!{1} = {2}".format(x, n, pow_fact_iter(x, n)))
input()
