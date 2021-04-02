# Task 5
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce


num_list = [i for i in range(100, 1001) if i % 2 == 0]
num_product = reduce(lambda n, m: n * m, num_list)


print("That number is horrifying: ", num_product)
