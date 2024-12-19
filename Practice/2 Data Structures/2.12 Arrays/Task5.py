class Array:
    """
    Линейный ститический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполненного массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def remove(self, value):
        pass
        # Добавьте ваш код тут
        indx = None
        i = 0
        
        while i <= self.length - 1:
            if self.data[i] == value:
                indx = i
                break
            i += 1
        
        if indx is not None:
            while indx < self.length - 1:
                self.data[indx] = self.data[indx + 1]

                indx += 1

            self.length -= 1

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"