
# Задание 3

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


def getting_sum(n):  # getting the number we need
    nn = int(n + n)
    nnn = int(n + n + n)
    what_we_seek = int(n) + nn + nnn
    return what_we_seek


num = input("Please enter a one-digit number: ")  # The number to be tortured
#  (one-digit just for the sake of practice)

if len(num) == 1:
    print(f"And the winner is.. {getting_sum(num)}!")
else:
    num = input("Please learn how to count till one and make another attempt to enter a one-digit number: ")
    if len(num) == 1:
        print(f"You've made it!\nAnd the winner is.. {getting_sum(num)}!")
    else:
        num_long = getting_sum(num)
        print(f"You know nothing, Jon Snow..\nBut if you insist: {num_long}")
