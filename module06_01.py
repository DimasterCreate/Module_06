class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}, теперь {self.name} сытый')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}, {self.name} умер')
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}, теперь {self.name} сытый')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}, {self.name} умер')
            self.alive = False
class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

Lion = Predator('Лев')
Cat = Mammal('Кот')
Cactus = Flower('Кактус')
Mango = Fruit('Манго')

print(Lion.alive)
print(Cat.fed)

Lion.eat(Cactus)
Cat.eat(Mango)

print(Lion.alive)
print(Cat.fed)

