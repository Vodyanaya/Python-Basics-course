# Task 3

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# I believe it's very far from the best option

month = int(input("Please enter a month number between 1 and 12: \n"))

# Using dict

month_list = ['winter', 'spring', 'summer', 'autumn']
month_range = [i for i in range(1, 13)]
month_range.insert(0, 12)
month_val = []
for i in range(4):
    month_val.append(month_range[:3])
    for t in month_range[:3]:
        month_range.remove(t)

month_dict = dict(zip(month_list, month_val))

for k in month_dict:  #
    if month in month_dict[k]:
        print(f"\nLucky you, it's {k.capitalize()} here!")

# Using list

month_list = [n for n in month_dict]
month_range = [i for i in range(1, 13)]
month_range.insert(0, 12)

k = 3

for i in range(4):
    if month_range.index(month) <= k - 1:
        print(f"\nDon't you like {month_list[i]}?")
        break
    else:
        k += 3
