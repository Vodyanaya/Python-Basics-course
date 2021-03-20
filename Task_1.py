
# Задание 1

# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

random_var = [1, 2, 3]
random_var_0 = "I'm not quite sure, what I am supposed to do here"
random_var_1 = [n + 1 for n in random_var]

print(random_var_1)
print(random_var, "\n" + random_var_0)

number_1 = int(input("Random number more than 1: "))
random_string = str(input("Random animal: "))

print(number_1, random_string + "s")