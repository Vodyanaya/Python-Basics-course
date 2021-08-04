# Task 3

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# I believe it's very far from the best option

month = int(input("Please enter a month number between 1 and 12: \n"))


month_list = ['winter', 'spring', 'summer', 'autumn']
month_range = [i for i in range(1, 12)]
month_range.insert(0, 12)

# Using list

k = 3

for i in range(4):
    if month_range.index(month) <= k - 1:
        print(f"\nLucky you, it's {month_list[i].capitalize()} here!")
        break
    else:
        k += 3

# Using dict

month_val = []
k = 0

for i in range(4):
    month_val.append(month_range[k:k + 3])
    k += 3

month_dict = dict(zip(month_list, month_val))

for k in month_dict:  #
    if month in month_dict[k]:
        print(f"\nDon't you like {k.capitalize()}?")


