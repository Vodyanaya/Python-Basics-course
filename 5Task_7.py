# Task 7.

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json


firm_profit = {}
profitable = []
average_profit = {}

with open("lesson5_task7.txt", "r", encoding="utf-8") as firms:
    for i in firms:
        firm_info = i.split()
        firm_profit[firm_info[0]] = int(firm_info[2]) - int(firm_info[3])
    profitable = [firm_profit[i] for i in firm_profit if firm_profit[i] > 0]
    average_profit["average_profit"] = round(sum(profitable) / len(profitable))

general_info = [firm_profit, average_profit]

with open("lesson5_task7.json", "w") as firms_json:
    json.dump(general_info, firms_json)

json_str = json.dumps(general_info)

print(f'''
Here is the information on firms, their profit or its absence, and the average profit:
{json_str}
           ''')
