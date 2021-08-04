# Task 1

# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

life_universe_everything = 6 * 7
list_rand = ["random string", 3.14, ["life", "universe", "everything"], True, life_universe_everything]

for i in list_rand:
    print(type(i))
