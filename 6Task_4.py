# Task 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed: int = 1, color="black", name="Hearse", is_police: bool = False):
        self.speed = str(speed) + " km/h"
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} starts moving"

    def stop(self):
        return f"{self.name} stops"

    def turn_right(self):
        return f"{self.name} turns right"

    def turn_left(self):
        return f"{self.name} turns left"

    def u_turn(self):
        return f"{self.name} makes a U-turn"

    def show_speed(self):
        return f"{self.name} moves with a speed of {self.speed}"


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed

    def show_speed(self):
        cur_speed = f"{self.name} moves with a speed of {self.speed} km/h"
        if self.speed > 60:
            print(cur_speed + f"\nAnd that's at least {int(self.speed - 60)}"
                              f" km/h too much for a {type(self).__name__.lower()}")
        else:
            return cur_speed


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed

    def show_speed(self):
        cur_speed = f"{self.name} moves with a speed of {self.speed} km/h"
        if self.speed > 40:
            print(cur_speed + f"\nAnd that's at least {int(self.speed - 40)}"
                              f" km/h too much for a {type(self).__name__.lower()}, you know")
        else:
            return cur_speed


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


lincoln = TownCar(75, "grey", "Lincoln", False)
ferrari = SportCar(666, "red", "Ferrari", False)
belarus = WorkCar(42, "blue", "Belarus", False)
bmw = PoliceCar(10, "black and white", "BMW")

print(f"{ferrari.name}\'s current speed is {ferrari.speed}")
print(f"When {ferrari.go()} and goes with a speed of {ferrari.speed}, {bmw.go()} and chases {ferrari.name}")
print(f"If {bmw.turn_left()} {lincoln.stop()} and waits")
print(f"If it is {bmw.is_police} that {bmw.name} is a {type(bmw).__name__} it should be {bmw.color}")
print(f"When {lincoln.u_turn()} across the double solid lines, {bmw.turn_right()} to chase it")
print(f"\n")
belarus.show_speed()
print(f"\n")
lincoln.show_speed()
