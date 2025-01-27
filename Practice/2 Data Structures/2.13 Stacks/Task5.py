class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Двойной стек на базе статического массива.
    """
    def __init__(self, size):
        super().__init__(size)
        self._left_length = 0
        self._right_length = 0

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        # Добавьте ваш код тут
        if self.length and self._left_length:
            self.length -= 1
            self._left_length -= 1
            return self.data[self._left_length]

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        # Добавьте ваш код тут
        if self.length and self._right_length:
            self.length -= 1
            self._right_length -= 1
            return self.data[self.size - self._right_length - 1]

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        # Добавьте ваш код тут
        if self.length == self.size:
            raise OverflowError
        
        self.data[self._left_length] = value
        self.length +=1
        self._left_length += 1

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        # Добавьте ваш код тут
        if self.length == self.size:
            raise OverflowError
        
        self.data[self.size - self._right_length - 1] = value
        self._right_length += 1
        self.length += 1

    def clear(self):
        """
        Очищает стек.
        """
        self.length = self._left_length = self._right_length = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        Используем size, так как массив теперь заполняется с двух сторон.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"


stack = Stack(4)
stack.push_left(12)
stack.push_left(7)
stack.push_left(6)
stack.push_right(8)
#   stack.push_left(3) - OverflowError

print(stack.pop_left())

print(stack.pop_right())

print(stack.pop_right())
