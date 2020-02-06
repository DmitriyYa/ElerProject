# -*- coding: utf-8 -*-
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


def task():
    count = 0
    list = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            if list.count(i) == 0:
                count = count+i
                list.append(i)
    print(count)


if __name__ == '__main__':
    task()
