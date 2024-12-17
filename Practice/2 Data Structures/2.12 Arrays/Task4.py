class Array:
    """
    Линейный статический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
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

    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """
        # Добавьте ваш код тут.
        if self.length == self.size:
            raise OverflowError
        
        if index > self.length - 1:
            self.append(value)
            return
        
        lst = self.data[index:self.length]
        self.data[index] = value
        self.data[index + 1:self.length + 1] = lst
        self.length += 1

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
    

array = Array(5)
array.append(20)
array.append(10)
array.append(30)
array.insert(1, 40) # вставка на позицию 1
print(array)

array.insert(20, 50)  # Индекс за пределами массива.
print(array)

array.insert(2, 50)
