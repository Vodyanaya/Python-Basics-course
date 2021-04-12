# Task 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def get_list():
    list_temp = input("Enter numbers\nUse space as a divider\nEnter \"stop\" to.. well, stop\nYour numbers: ").split()
    return list_temp


def get_sum():
    out = 0
    list_sum = []
    while out == 0:
        list_temp = get_list()
        for i in list_temp:
            if i.lower() == "stop":
                out = 1
                print(f"\nThe final results would be: ")
                break
            elif not i.isdigit():
                print("\nNumbers..")
                continue
            else:
                list_sum.append(int(i))
        print(f"\nThe sum of the numbers entered: {sum(list_sum)}\n")
    print(f"The overall sum is {sum(list_sum)}")


get_sum()
