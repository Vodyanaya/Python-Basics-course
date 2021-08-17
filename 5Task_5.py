# Task 5.

# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randrange

with open("lesson5_task5.txt", "w", encoding="utf-8") as nums_to_get:
    nums = [str(randrange(1, 60)) for n in range(15)]
    print(nums)
    nums_to_record = ""
    for i in nums:
        nums_to_record += i + " "
    nums_to_get.writelines(nums_to_record)

# That is my understanding, that there should be calculated the sum of numbers retrieved from the file
# I might have gotten it wrong

with open("lesson5_task5.txt", "r", encoding="utf-8") as nums_to_process:
    nums_to_sum = nums_to_process.readline().split()
    print(f"The sum is {sum(map(int, nums_to_sum))}")
