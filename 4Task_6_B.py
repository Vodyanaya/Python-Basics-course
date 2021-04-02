# Task 6
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from sys import argv
from itertools import cycle

phrase_rand = argv[1]
k = 0
for i in cycle(phrase_rand):
    if k > 10:
        break
    print(i)
    k += 1
