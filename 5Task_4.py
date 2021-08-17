# Task 4.

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

text = open("lesson5_task4.txt", "r", encoding="utf-8")
lines = text.readlines()
text.close()

translation = {"One": "Один",
"Two": "Два",
"Three": "Три",
"Four": "Четыре"}

lines_rus = []
for i in lines:
    word = i.split()
    word_rus = i.replace(word[0], translation[word[0]])
    lines_rus.append(word_rus)
print(lines_rus)

with open("lesson5_task4_rus.txt", "w", encoding="utf-8") as text_to_record:
    text_to_record.writelines(lines_rus)
