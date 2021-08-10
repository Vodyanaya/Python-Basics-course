# Task 4.
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    result = x**y
    return result


def my_func_1(x, y):
    m = 1
    for i in range(abs(y)):
        m = m * x
    return 1 / m


num_R = float(input("A positive number: "))
num_power = int(input("A negative integer: "))

print("The result is:", "\n" + format(my_func(num_R, num_power)))
print("The result is:", "\n" + format(my_func_1(num_R, num_power)))
