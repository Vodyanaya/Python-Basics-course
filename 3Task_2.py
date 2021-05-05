# Task 2.

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def get_info(**kwargs):
    result_line = [i for i in kwargs.values()]
    return " ".join(result_line)


def get_info_1(**kwargs):
    line_result = []
    for param, data in kwargs.items():
        param = param.replace("_", " ")
        line_temp = f"{param}: {data},"
        line_result.append(line_temp)
    return " ".join(line_result).rstrip(",")


print(get_info(name="Anakin", surname="Skywalker", year_of_birth="41 BBY", city_of_residence="the Death Star",
               email="darthkitty99@gmail.com", phone="424242"))

print(get_info_1(name="Anakin", surname="Skywalker", year_of_birth="41 BBY",
                 city_of_residence="the Death Star",
                 email="darthkitty99@gmail.com", phone="424242"))
