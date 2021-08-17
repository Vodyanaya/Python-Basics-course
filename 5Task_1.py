# Task 1.

# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open("lesson5_task1.txt", "w", encoding="utf-8") as text_to_have:
    while True:
        input_line = input("Text you want to be recorded: \n")
        if input_line:
            text_to_have.writelines(input_line)
        else:
            break

with open("lesson5_task1.txt", "r", encoding="utf-8") as text_to_read:
    text = text_to_read.read()
print(text)
