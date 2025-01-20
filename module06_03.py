import random
from random import randint


class Animal:
    alive = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def move(self, dx, dy, dz):
        new_cords = [dx * self.speed, dy * self.speed, dz * self.speed]
        self._cords = [x+y for x,y in zip(self._cords, new_cords)]
        if self._cords[2] < 0:
            print('Это слишком глубоко, я не умею плавать')
            self._cords = [x - y for x, y in zip(self._cords, new_cords)]
    def get_cords(self):
        return print(f'Координаты животного "{self.name}" X: {self._cords[0]},  Y: {self._cords[1]}, '
                f' Z: {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Прости, я мирный')
        else:
            print('Будь осторожен, я на тебя нападу')

    def speak(self):
        return print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        return print(f'Здесь {randint(1,4)} яиц для тебя')
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal,AquaticAnimal, Bird):
    sound = 'Click Click Click'



db = Duckbill('Утконос', 10)
print(db.alive)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
