# Task 2.

# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

from string import punctuation


# Solely for the sake of practice
def get_clean_lines(arg: list):
    clean_lines = []
    for elem in arg:
        if elem != "\n":
            clean_lines.append(elem.strip("\n").strip(punctuation).replace(",", ""))
    return clean_lines


def get_words_in_line(arg: list):
    words_in_line = {}
    for elem in arg:
        words_in_line[elem] = len(elem.split())
    return words_in_line


text_to_read = open("lesson5_task2.txt", "r", encoding="utf-8")
print(f"The document:\n{text_to_read.read()}\n")
text_to_read.close()


with open("lesson5_task2.txt", "r", encoding="utf-8") as text_to_read:
    text_to_process = text_to_read.readlines()
    sentences = get_clean_lines(text_to_process)
    num_of_lines = len(sentences)
    num_of_words = get_words_in_line(sentences)


print(f"There are {num_of_lines} lines in the document\n")

k = 1
for i in num_of_words.values():
    print(f"There are {i} words in the line number {k}")
    k += 1
