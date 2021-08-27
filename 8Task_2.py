# Task 2.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyDivisionError(Exception):
    text = '''It's raining men! Hallelujah!...
    Or it's division by zero'''

    def __str__(self):
        return self.text


class Division(float):

    def __truediv__(self, other):
        if other == 0:
            raise MyDivisionError
        else:
            return Division((float(self) / float(other)))


try:
    dividend, divisor = Division(input("Enter a dividend: ")), Division(input("Enter a divisor: "))
    print(round(dividend / divisor))
except MyDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
