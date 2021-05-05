# Task 1.

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# I'm not sure I got the task right

def get_nums():
    try:
        num_1 = float(input("enter a number to be divided: "))
        num_2 = float(input("enter a divider: "))
        out_num = num_1 / num_2
    except ValueError:
        return "Are you sure, these are both numbers?"
    except ZeroDivisionError:
        return "That's not something we can do here"
    return out_num


print(round(get_nums(), 2))  # Two digits just as an example
