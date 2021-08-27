# Task 1.
# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date: str):
        self.day, self.month, self.year = self.get_date(date)
        if not self.validate(date):
            raise ValueError(f"{date} is not a date within the given conditions")

    @classmethod
    def get_date(cls, date: str):
        return [int(i) for i in date.split("-")]

    @staticmethod
    def validate(date: str):
        day, month, year = Date.get_date(date)
        return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2200

    def __str__(self):
        return f"The date is {self.day}.{self.month}.{self.year}"


today = Date('27-08-2021')
print(Date.validate("27-08-2021"))
print(Date.get_date("27-08-2021"))
print(Date.validate("27-08-3021"))
tomorrow = Date("25-201-2020") # error
