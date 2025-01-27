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
    Стек на базе статического массива.
    """

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Добавьте ваш код тут
        if self.length:
            elem = self.data[self.length - 1]
            self.length -= 1
            return elem

    def push(self, value):
        """
        Добавялет элемент со значением value в стек.
        """
        # Добавьте ваш код тут
        if self.length == self.size:
            raise OverflowError
        
        self.data[self.length] = value
        self.length += 1

stack = Stack(3)
stack.push(12)
stack.push(7)
stack.push(6)
#   stack.push(8) - OverflowError

print(stack.pop())

print(stack.pop())

print(stack.pop())

print(stack.pop())
