# Task 3
#  Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
#  Необходимо решить задание в одну строку.

# including 240

num_list = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]

print(num_list)

# Alternatively as a single line solution

# print([n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0])
