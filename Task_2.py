
# Задание 2

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


def zero_for_num(f):  # puts zero where it's missing
    if len(f) == 1:
        f = "0" + f
    return f


time_in_sec = int(input("your time in seconds "))  # number to be tortured

hh = str(int(time_in_sec // 3600))  # hours
mm = str(int(time_in_sec % 3600 / 60))  # minutes
ss = str(int(time_in_sec % 60))  # seconds

# hh = "0" + hh if len(hh) == 1 else hh # remembering how it can be done (sorry)
# mm = "0" + mm if len(mm) == 1 else mm
hh = zero_for_num(hh)
mm = zero_for_num(mm)
ss = zero_for_num(ss)

print('{}:{}:{}'.format(hh, mm, ss))


# Задание 2.2


# import datetime

# time_in_sec = int(input("your time in seconds "))

# hh = int(time_in_sec // 3600)  # hours
# mm = int(time_in_sec % 3600 / 60) # minutes
# ss = int(time_in_sec % 60) # seconds

# time_form = datetime.time(hh, mm, ss)
# print(time_form)
