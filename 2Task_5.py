# Task 5

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# Task 5.1

from random import randint


def get_ind(list_n, n):  # getting index
    k = list_n.count(n)
    last_ind = list_n.index(n) + k - 1
    return last_ind


def get_pretty(a):  # getting nicer version of text
    nice = ' '.join([str(let) for let in a])
    return nice


num_range = []  # getting random "rating"
for i in range(12):
    num_range.append(randint(1, 11))

answer = input(
    "We have a rating here and can rate your number against it."
    "\nType \"No\" if you are strongly against it.\nPlease enter a number to rate: ")

if answer.lower() != "no":
    try:
        number = int(answer)
    except ValueError:
        print("Sorry, only numbers")
    else:
        num_range.append(number)
        num_range.sort(reverse=True)
        ind = get_ind(num_range, number)
        before_rate = get_pretty(num_range[:ind])
        after_rate = get_pretty(num_range[ind + 1:])
        print(f"See, where your number fits:\n {before_rate} *- {num_range[ind]} -* {after_rate}")
else:
    print("Pity")

# Task 5.2

# At first I've misunderstood what is there to be done
# I've decided to leave it just in case

# 
# num_range = []
# while True:
#         answer = input(
#         "We rate numbers here. Type \"No\" if you are strongly against it.
#         "\nPlease enter a number to rate: ")
#         if answer.lower() == "no":
#             break
#         else:
#             try:
#                 number = int(answer)
#             except ValueError:
#                 print("\nAre you sure it's a number?")
#             else:
#                 num_range.append(number)
#                 num_range.sort(reverse=True)
#                 print(f"See, where your number fits{num_range}")
#
