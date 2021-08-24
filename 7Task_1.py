#  Task 1
# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from random import randint


def get_matrix(rows, columns, limit=99):
    matrix = []
    for r in range(rows):
        matrix.append([])
        for c in range(columns):
            matrix[r].append(randint(1, limit))
    return matrix


class Matrix:
    def __init__(self, rows: list):
        self.rows = rows

    def __str__(self):
        return "\n".join(str(row).replace(',', '').strip('[]') for row in self.rows)

    def __add__(self, other):
        try:
            rows_num = len(self.rows)
            columns_num = len(self.rows[0])
            new_matrix = []
            for row in range(rows_num):
                new_matrix.append([])
                for column in range(columns_num):
                    new_matrix[row].append(self.rows[row][column] + other.rows[row][column])
            return Matrix(new_matrix)
        except IndexError:
            print("The matrices do not much. That's not appreciated")


matrix_1,  matrix_2 = Matrix(get_matrix(3, 3)), Matrix(get_matrix(3, 3, 1))

print(f"Matrix 1: \n{matrix_1}\nMatrix 2: \n{matrix_2}")
print(f"The result Matrix: \n{matrix_1 + matrix_2}")
