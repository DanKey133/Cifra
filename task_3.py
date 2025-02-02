class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._name

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        # все необходимые проверки
        if isinstance(pages, int):
            self._pages = pages
        else:
            raise TypeError("Количество страниц должно быть типа int")

    def __repr__(self):
        return super().__repr__()[:-1] + f', pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._pages

    @duration.setter
    def duration(self, duration: int):
        # все необходимые проверки
        if isinstance(duration, float):
            self._pages = duration
        else:
            raise TypeError("Длительность аудиокниги должна быть типа float")

    def __repr__(self):
        return super().__repr__()[:-2] + f', dutration={self.duration})'


paper_book = PaperBook(name='Война и мир', author='Лев Толстой', pages=5202)
audio_book = AudioBook(name='Война и мир', author='Лев Толстой', duration=76.22)

#проверка инициазиции объектов
#paper_book = PaperBook(name='Война и мир', author='Лев Толстой', pages=5202.1)
#audio_book = AudioBook(name='Война и мир', author='Лев Толстой', duration='76')

#paper_book.name = 'Преступление и наказание' # проверка защиты от изменения пользователем
#audio_book.author = 'Достоевский' # проверка защиты от изменения пользователем


print(paper_book, '\n', audio_book, sep='')
print([paper_book])
print([audio_book])

