# Task 6

#
# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


# Unfortunately, I have issues with Russian layout currently, but I've tried my best
# And I'm not sure whether I got the task correctly

def get_pretty(a):
    nice = ', '.join([str(sym) for sym in a])
    return nice


def get_info():
    pos_param = ["название", "цена", "количество", "единица измерения"]  # Position parameters
    pos_param_values = []
    for nam in pos_param:
        param_nam = input(f"{nam.capitalize()}: ")
        pos_param_values.append(param_nam)
    pos_info = dict(zip(pos_param, pos_param_values))
    return pos_info


positions = []
k = 1

while input("Добавить товар, (да/нет): ") == "да".lower():
    pos_temp = [k, get_info()]
    pos_temp = tuple(pos_temp)
    positions.append(pos_temp)
    k += 1

#     Необходимо собрать аналитику о товарах.
#     Реализовать словарь, в котором каждый ключ — характеристика товара,
#     например название, а значение — список значений-характеристик, например список названий товаров.

# print(positions)  # The list of tuples  itself

if len(positions) != 0:
    print(f"Позиции:\n{get_pretty(positions):<10}\n")
    position_param = [n for n in positions[0][1].keys()]
    all_positions = {}
    for n in position_param:
        temp = []
        for i in range(len(positions)):
            val = positions[i][1][n]
            if val not in temp:
                temp.append(val)
                all_positions[n] = temp
#    print(all_positions)  # Regular output
    for i in all_positions.keys():  # Alternative output
        print(f"{i}: \n{get_pretty(all_positions[i]):>3}")
else:
    print("Товаров нет")
