# Task 4
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

from random import randrange
from itertools import filterfalse

num_range = [] 
for i in range(15):
    num_range.append(randrange(1, 60))

print(num_range)

for n in num_range:
    if num_range.count(n) > 1:
        num_range = list(filterfalse(lambda m: m == n, num_range))

print(num_range)
