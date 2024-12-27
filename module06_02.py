class Vehicle:
    __COLOR_VARIANTS = ['зеленый', 'красный', 'голубой', 'бардовый', 'серый']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = str(__engine_power)
        self.__color = str(__color)
    def get_model(self):
        print(f'Модель автомобиля: {self.__model}')
    def get_ep(self):
        print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        print(f'Цвет кузова: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_ep()
        self.get_color()
        print(f'Владелец: {self.owner}\n')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['зеленый', 'красный', 'голубой', 'бардовый', 'серый']
car1 = Sedan('Григорий', 'Лада 2114', 100, 'серый')

# Изначальные свойства
car1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
car1.set_color('оранжевый')
car1.set_color('красный')
car1.owner = 'Арсений'

# Проверяем что поменялось
car1.print_info()

