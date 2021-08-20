# Task 1.
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:

    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def running(self):
        for i in range(3):
            phase_now = self.__color[i]
            print(f"{phase_now.capitalize()}")
            if phase_now == "red":
                print("{:>13}".format("Stop"))
                time.sleep(7)
            elif phase_now == "yellow":
                print("{:>13}".format("Wait"))
                time.sleep(2)
            elif phase_now == "green":
                print("{:>13}".format("Go"))
                time.sleep(9)
            i += 1


crossing = TrafficLight()
# print(light.running())

k = 0
while k < 3:
    crossing.running()
    k += 1
