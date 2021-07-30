
# Задание 4

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


number = int(input("Please enter a positive number: "))
while number < 0:
    number = int(input("Please enter a positive number: "))


# Option 1

list_num = [int(n) for n in str(number)]
# print(max(list_num))

max_num = 0
i = 0

while i < len(list_num):
    if list_num[i] > max_num:
        max_num = list_num[i]
    i += 1

print(max_num)


# Option 2

max_num = 0
while number > 0:
    digit = number % 10
    number = number // 10
    if digit > max_num:
        max_num = digit

print(max_num)


