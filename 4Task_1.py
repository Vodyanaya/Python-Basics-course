# Task 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, h_rate, bonus = argv

print("The script is ", script_name)
print("Employee is getting: ", int(hours) * int(h_rate) + int(bonus))
