# Task 6
# а) итератор, генерирующий целые числа, начиная с указанного

from sys import argv
from itertools import count

script_name, ind = argv

print("the script: ", script_name)
for i in count(ind):
    if i > ind + 15:
        break
    else:
        print(i)
