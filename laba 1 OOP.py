# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Reservoir:

    def __init__(self, volume: float, volume_max:float):
        """
        Устанавливает и осуществляет валидацию входных данных в объект
        резервуара
        :param volume: Текущий объем нефти в резервуаре
        :param volume_max: Объем резервуара
        """
        if volume < 0 or volume_max < 0:
            print('Ошибка входных данных!')
        self.volume = volume
        self.volume_max = volume_max

    def is_reservoir_full(self) -> bool:
        """
        Метод проверяет заполнение резервуара. Если резервуар заполнен нефтью полностью,
        то объем нефти остается постоянной величино и выводится предупреждение.
        >>> pump = Pump(10)
        >>> pipe = Pipe(pump.flow_rate)
        >>> reservoir = Reservoir(50, 500)
        >>> print(reservoir.is_reservoir_full()) #False
        :return: False - если резервуар заполнен не полностью. Иначе True.
        """
        if self.volume < self.volume_max:
            return False
        print('ВНИМАНИЕ ПЕРЕПОЛНЕНИЕ РЕЗЕРВУАРА!')
        self.volume = self.volume_max
        return True

    def add_oil(self, vol_oil:float):
        """
        Добавляет или откачивает нефть из резервуара
        :param vol_oil: объем вкаченной/откаченной нефти
        """
        if pipe.is_open and pump.button:
            self.volume += pipe.flow_rate
            self.is_reservoir_full()


class Pump:

    def __init__(self, flow_rate: float, button: bool=False):
        """
        Устанавливает и осуществляет валидацию входных данных в объект
        насоса
        :param flow_rate: дебит насоса
        :param button: кнопка включения (True) и выключения насоса (False)
        """
        self.flow_rate =  flow_rate
        self.button = button

    def turn_the_button(self):
        """
        Включает и выключает насос
        """
        self.button = not self.button

    def super_(self):
        """
        Удваивает мощность насоса
        """
        self.flow_rate = 2 * self.flow_rate

class Pipe:

    def __init__(self, flow_rate: float, leak: float=0, is_open: bool=False):
        """
        Устанавливает и осуществляет валидацию входных данных в объект
        трубы
        :param flow_rate: поток через трубу
        :param leak: утечка из трубы
        :param is_open: перекрыта труба (False) или открыта (True)
        """
        if leak > 0:
            print('Ошибка во входных данных!')
        self.leak = leak
        self.is_open = is_open
        self.flow_rate = flow_rate

    def leaking(self):
        """
        Добавляет утечку из трубы
        """
        self.flow_rate = self.flow_rate - self.leak

    def close_or_open(self):
        """
        Перекрывает или открывает трубу
        """
        self.is_open = not self.is_open

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

