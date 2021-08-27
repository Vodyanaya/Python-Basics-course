# Task  7.
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
#
class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"

    def __str__(self):
        return f"{self.a} + {self.b} * i"


num_1 = ComplexNum(1, -2)
num_2 = ComplexNum(5, 3)
print(num_1 + num_2)
print(num_1 * num_2)
print(num_1)
print(num_2)
