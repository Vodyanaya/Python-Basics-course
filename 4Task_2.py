# Task 2
# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

from random import randint

num_range = []
for i in range(15):
    num_range.append(randint(1, 300))

num_find = []
for i in num_range[1:]:
    num_prev = num_range[num_range.index(i) - 1]
    if i > num_prev:
        num_find.append(i)

print(f"The list:\n{num_range}\nThe elements needed:\n{num_find}")
