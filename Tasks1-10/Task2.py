# -*- coding: utf-8 -*-
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
import time




def fibonacci(n):
    fib1, fib2 = 1, 1
    ef1, ef2 = 1, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2

        yield fib1


def task(n):
    count = 0
    for fib in fibonacci(n):
        if fib % 2 == 0:
            count = count+fib
    print(count)

if __name__ == '__main__':
    # task(100)
    print(time.time())
    for i in fibonacci(4000000-1):
        pass
    print(i)
    print(time.time())
