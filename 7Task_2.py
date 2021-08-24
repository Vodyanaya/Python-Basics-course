# Task 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str, parameter):
        self.parameter = parameter
        self.name = name

    @property
    @abstractmethod
    def fabric(self):
        pass

    def __add__(self, other):
        return self.fabric + other.fabric


class Coat(Clothes):

    @property
    def fabric(self):
        return round(self.parameter / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def fabric(self):
        return round(2 * self.parameter + 0.3, 2)


coat = Coat("Invisibility cloak", 42)
print(coat.fabric)

suit = Suit("Batsuit", 1.96)
print(suit.fabric)

print(coat + suit)
