# Программа вычесляет элементы фибоначи
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.3.2020

def get_input(msg):
    return input(msg)


def fibonachi_rec(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonachi_rec(n - 1) + fibonachi_rec(n - 2)


def fibonachi_elem(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        c = a
        a = b
        b += c
        i += 1
    return c


def output_to_user(msg="", s="", e="\n"):
    print(msg, sep=s, end=e)


def all_fib(n, k=1):
    for i in range(k, n + 1):
        output_to_user(fibonachi_elem(i), e=" ")
    output_to_user()


def build_to_int(var):
    if not (isinstance(var, str) and var.isdigit()):
        return None
    return int(var)


def main():
    while True:
        task = get_input("Input command\n"
                         "1 - Output one element recursion\n"
                         "2 - Output to the specified element\n"
                         "3 - Output part of sequence\n"
                         "4 - Exit\n")
        if task == "1":
            n = build_to_int(get_input("Input number of element: "))
            if n:
                print(fibonachi_rec(n-1))

        elif task == "2":
            n = build_to_int(get_input("Input number of element: "))
            if n:
                all_fib(n)

        elif task == "3":
            k = build_to_int(get_input("Input Start: "))
            n = build_to_int(get_input("Input End: "))
            if n and k:
                all_fib(n, k)
        elif task == "4":
            break


if __name__ == "__main__":
    main()
