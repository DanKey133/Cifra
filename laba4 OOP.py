import doctest

class Ship:

    def __init__(self, name:str, weight_max:float, velocity:float) -> None:
        """
        Создание и подготовка к работе класса гражданский корабль
        :param name: Название судна
        :param weight_max: Грузоподъемность в тоннах
        :param velocity: Максимальная скорость в км/ч

        Пример:
        >>> ship = Ship(name='Победа', weight_max=120, velocity=34)
        """
        self.type = 'Гражданский'
        self.weight_max = weight_max
        self.velocity =  velocity
        self.name = name
        self.weight = 0 #переменная текущего веса (изначально 0)

    def __repr__(self) -> str:
        """Представление объекта гражжданский корабль"""
        return f"Ship(type={self.type}, name={self.name}, weight_max={self.weight_max}, velocity={self.velocity})"

    def __str__(self) -> str:
        """Описание объекта гражданский корабль"""
        return f"'{self.name}'({self.type}):\nГрузоподъемность = {self.weight_max} т.\nСкорость = {self.velocity} км/ч,\nЗагрузка = {self.weight} т."

    def load_ship(self, mass:float) -> None:
        """
        Функция добавления груза на корабль и проверки допустимой грузоподъемности
        :param mass: Масса груза, тонны

        Пример:
        >>> ship = Ship(name='Победа', weight_max=120, velocity=34)
        >>> ship.load_ship(110)
        """
        if self.weight + mass > self.weight_max:
            self.weight = self.weight_max
            print('Корабль нагружен по максимуму!')
        else:
            self.weight += mass

    def unload_ship(self, mass:float)->None:
        """
        Функция удаления згруза с корабля с соответствующими проверками
        :param mass: Масса груза, тонны

        Пример:
        >>> ship = Ship(name='Победа', weight_max=120, velocity=34)
        >>> ship.load_ship(110)
        >>> ship.unload_ship(30)
        """
        if self.weight - mass < 0:
            self.weight = 0
            print('Корабль полностью разгружен!')
        else:
            self.weight -= mass



class WarShip(Ship):

    def __init__(self, name:str, weight_max:float, velocity:float, bullets:int) -> None:
        """
        Базовый класс военного корабля
        :param name: Название судна
        :param weight_max: Грузоподъемность в тоннах
        :param velocity: Максимальная скорость в км/ч
        :param bullets:  Число снарядов, шт.

        Пример:
        >>> war_ship = WarShip(name='Беда', weight_max=120, velocity=34, bullets=3)
        """
        super().__init__(name, weight_max, velocity)
        self.type = 'Военный'
        self.bullets = bullets

    def __str__(self) -> str:
        """
        Описание объекта военный корабль
        Перегружаем метод, так как появился новый атрибут bullets
        """
        return super().__str__() + f"\nЧисло зарядов = {self.bullets}"

    def __repr__(self) -> str:
        """
        Представление объекта военный корабль
        Перегружаем метод, так как появился новый атрибут bullets
        """
        return super().__repr__()[:-1] + f", bullets={self.bullets})"

    def load_ship(self, mass:float, bullets:int=0) -> None:
        """
        Функция добавления груза и снарядов на корабль, а также проверки допустимой грузоподъемности
        Перегружаем метод, добавляем возможность загрузки числа снарядов
        :param mass: Масса груза, тонны
        :param bullets: Число снарядов, шт.

        Пример:
        >>> war_ship = WarShip(name='Беда', weight_max=120, velocity=34, bullets=3)
        >>> war_ship.load_ship(20, 3)
        """
        super().load_ship(mass)
        self.bullets += bullets

    def shoot(self, shots:int) -> None:
        """
        Функция выстрела. Уменьшает число снарядов и оповещает о выстреле
        :param shots:

        Пример:
        >>> war_ship = WarShip(name='Беда', weight_max=120, velocity=34, bullets=3)
        >>> war_ship.shoot(3)
        Выстрел!

        """
        # проверка числа снарядов
        if self.bullets == 0:
            print('Снарядов не осталось!')
        elif shots > self.bullets:
            self.bullets = 0
            print('Выстрел!')
        else:
            self.bullets -= shots #уменьшаем число снарядов
            print('Выстрел!')

if __name__ == "__main__":

    ship = Ship(name='Победа', weight_max=120, velocity=34)
    war_ship = WarShip(name='Беда', weight_max=120, velocity=34, bullets=3)
    print(ship, war_ship, sep='\n\n')
    print([ship], [war_ship], sep='\n')

    ship.load_ship(130)
    ship.unload_ship(30)
    ship.unload_ship(110)
    print(ship.weight)

    war_ship.load_ship(130)
    war_ship.unload_ship(30)
    war_ship.unload_ship(110)
    print(war_ship.weight)

    war_ship.shoot(1)
    war_ship.shoot(2)
    war_ship.shoot(3)
    war_ship.load_ship(20, 3)
    war_ship.shoot(3)

    doctest.testmod()





