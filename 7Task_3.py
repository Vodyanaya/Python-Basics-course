# Task 3
# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание.
# Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение.
# Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление.
# Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:

    def __init__(self, nuclei: int):
        self._nuclei = nuclei

    def check_class(self, other):
        assert isinstance(other, self.__class__), "Applicable to Cells only"

    def __str__(self):
        return f"This cell contains {self._nuclei} nucleus" \
            if self._nuclei == 1 else f"This cell contains {self._nuclei} nuclei"

    def __add__(self, other: "Cell"):
        self.check_class(other)
        result = self._nuclei + other._nuclei
        return Cell(result)

    def __sub__(self, other: "Cell"):
        self.check_class(other)
        if self._nuclei > other._nuclei:
            return Cell(self._nuclei - other._nuclei)
        else:
            return "A cell can't have a negative amount of nuclei"

    def __mul__(self, other: "Cell"):
        self.check_class(other)
        result = self._nuclei * other._nuclei
        return Cell(result)

    def __truediv__(self, other: "Cell"):
        self.check_class(other)
        result = self._nuclei // other._nuclei
        return Cell(round(result))

    def make_order(self, row_length):
        chars = "*" * self._nuclei
        rows = "\n".join([chars[i:i + row_length] for i in range(0, len(chars), row_length)])
        return rows


cell_1, cell_2, cell_3 = Cell(16), Cell(4), Cell(2)

print(f'''
    {cell_2 + cell_1}
    {cell_3 - cell_2}
    {cell_2 / cell_3}
    {cell_2 * cell_1}
''')

print(Cell.make_order(cell_1, 3))
