
# Задание 4

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.


number = int(input("Please enter a positive number: "))
while number < 0:
    number = int(input("Please enter a positive number: "))

list_num = [int(n) for n in str(number)]
# print(max(list_num))

max_num = 0
i = 0

while i < len(list_num):
    if list_num[i] > max_num:
        max_num = list_num[i]
    i += 1

print(max_num)
