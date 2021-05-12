# Task 3.

# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open("lesson5_task3.txt", "r", encoding="utf-8") as text_to_read:
    text_to_process = text_to_read.readlines()

employees_info = {}
for elem in text_to_process:
    elem = elem.split()
    employees_info[elem[0]] = int(elem[1])

poor_employees = []
for i in employees_info:
    if employees_info[i] < 20000:
        poor_employees.append(i)


print(f"The mean wage is {sum(employees_info.values())/len(employees_info)}")
print(f"The following guys are getting less than 20000 mysterious coins: {poor_employees}")
