class Vehicle:
    __COLOR_VARIANTS = (blue, red, pink, green)
    def __init__(self, owner, model, color, engine_power):
        def get_model(self):
            return f'Модель: {self.__model}'

        def get_horsepower(self):
            return f'Мощность двигателя: {self.__engine_power}'

        def get_color(self):
            return f'цвет:{self.__color}'

def print_info(self):
    print('\033[34m', self.get_model())
    print(self.get_horsepower())
    print(self.get_color())
    print('Владелец:',self.onwer)


    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\033[37mНельзя сменить цвет на {new_color}')

            class Sedan:
                __PASSENGERS_LIMIT = 5
                # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
                vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

                # Изначальные свойства
                vehicle1.print_info()

                # Меняем свойства (в т.ч. вызывая методы)
                vehicle1.set_color('Pink')
                vehicle1.set_color('BLACK')
                vehicle1.owner = 'Vasyok'

                # Проверяем что поменялось
                vehicle1.print_info()