# Task 1.

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# I'm not sure I got the task right


def get_num(dividend, divisor):
    try:
        out_num = float(dividend) / float(divisor)
    except ValueError:
        return "Are you sure, these are both numbers?"
    except ZeroDivisionError:
        return "That's not something we can do here"
    else:
        return round(out_num, 2)  # Two digits just as an example


num_1, num_2 = input("enter a number to be divided: "), input("enter a divider: ")
print(get_num(num_1, num_2))
