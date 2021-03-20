
# Задание 3

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


def getting_sum(n):  # getting the number we need
    nn = int(n + n)
    nnn = int(n + n + n)
    what_we_seek = int(n) + nn + nnn
    return what_we_seek


i = str(int(input("Please enter a one-digit number: ")))  # The number to be tortured
#  (one-digit just for the sake of practice)

if len(i) == 1:
    print(f"And the winner is.. {getting_sum(i)}!")
else:
    i = str(int(input("Please learn how to count till one and make another attempt to enter a one-digit number: ")))
    if len(i) == 1:
        print(f"You've made it!\nAnd the winner is.. {getting_sum(i)}!")
    else:
        num_long = getting_sum(i)
        print(f"You know nothing, Jon Snow..\nBut if you insist: {num_long}")

