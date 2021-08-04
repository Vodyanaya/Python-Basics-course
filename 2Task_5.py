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


def get_pretty(a):  # getting nicer version of text for the output
    nice = ' '.join([str(let) for let in a])
    return nice


num_range = []  # getting random "rating" (For the sake of practice)
for i in range(12):
    num_range.append(randint(1, 11))
num_range.sort(reverse=True)


answer = input(
    "We have a rating here and can rate your number against it."
    "\nType \"No\" if you are strongly against it.\nPlease enter a number to rate: ")


if answer.lower() != "no":
    try:
        number = int(answer)
    except ValueError:
        print("Sorry, only numbers")
    else:
        for i in num_range:
            if i < number:
                ind = num_range.index(i)
                num_range.insert(ind, number)
                before_rate = get_pretty(num_range[:ind])
                after_rate = get_pretty(num_range[ind + 1:])
                print(f"See, where your number fits:\n {before_rate} *- {num_range[ind]} -* {after_rate}")
                break
else:
    print("Pity")
