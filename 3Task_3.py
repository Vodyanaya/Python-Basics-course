# Task 3
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    num_list = [a, b, c]
    num_list.sort(reverse=True)
    sum_num = num_list[0] + num_list[1]
    return f"The sum of the two greatest numbers is {sum_num}"


#  For the sake of practice

numbs = []
try:
    for i in range(3):
        num = int(input(f"number {i + 1}:\n "))
        numbs.append(num)
    print(my_func(numbs[0], numbs[1], numbs[2]))
except ValueError:
    print("Are you sure, these are all numbers?")
    pass
