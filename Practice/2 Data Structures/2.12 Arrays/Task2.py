class Array:
    """
    Линейный статический массив.
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

    def min(self):
        """
        Минимальное значение в массиве.
        """
        # Добавьте ваш код тут
        min_value = self.data[0]

        for i in range(self.length):
            if self.data[i] < min_value:
                min_value = self.data[i]

        return min_value

    def max(self):
        """
        Максимальное значение в массиве.
        """
        # Добавьте ваш код тут
        max_value = self.data[0]

        for i in range(self.length):
            if self.data[i] > max_value:
                max_value = self.data[i]

        return max_value

    def avg(self):
        """
        Среднее значение в массиве.
        """
        # Добавьте ваш код тут
        total_sum = 0

        for i in range(self.length):
            total_sum += self.data[i]

        return total_sum / self.length

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
    