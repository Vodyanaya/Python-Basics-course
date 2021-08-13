# Task 6
# а) итератор, генерирующий целые числа, начиная с указанного

from sys import argv
from itertools import count

script_name, num = argv

print(f"Count starts from {num}")

num = int(num)

for i in count(num):
    if i > num + 15:
        break
    else:
        print(i)
