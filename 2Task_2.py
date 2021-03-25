# Task 2

# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


elements = [n for n in
            input("Please enter a list of \'whatnot\', use space as separator: ").split()]  # list of elements

for ind in range(len(elements)):  # range of indices
    if ind % 2 != 0:  # odd index
        less_ind = ind - 1  # even index
        elem = elements[less_ind]  # storing previous value
        elements[less_ind] = elements[ind]  # assigning new value
        elements[ind] = elem  # assigning stored value

print(elements)

# Task 2.2
# as expected, if elements are repeated, it doesn't work properly

# for elem in elements:
#     if elements.index(elem) % 2 != 0:
#         less_ind = elements.index(elem) - 1
#         elements[elements.index(elem)] = elements[less_ind]
#         elements[less_ind] = elem
# print(elements)
