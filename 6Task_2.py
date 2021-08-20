# Task 2.
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, _length, _width, _thick=5):
        self._length = _length
        self._width = _width
        self._thick = _thick
        self.__mass_gost = 25
        self.asphalt = self._length * self._width * self._thick * self.__mass_gost

    def get_mass(self):
        if self.asphalt > 1000:
            print(f"You need {self.asphalt / 1000} tonnes of asphalt")
        elif self.asphalt == 1000:
            print(f"You need {int(self.asphalt / 1000)} tonne of asphalt")
        else:
            print(f"You need {self.asphalt} kg of asphalt")


asphalt = Road(20, 5000)
asphalt.get_mass()
