# Task 7.
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

import math


def fact(m):
    for el in range(1, m + 1):
        yield math.factorial(el)


n = int(input("Enter a number: "))

k = 0
for i in fact(n):
    print(f"{k + 1}! = {i}")
    k += 1
