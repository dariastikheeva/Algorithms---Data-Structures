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


class Queue(Array):
    """
    Очередь на базе статического массива.
    """
    def __init__(self, size):
        super().__init__(size)
        # указатель на последний добавленный элемент
        self.last = -1
        # указатель на первый элемент в очереди
        self.first = -1

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        # Добавьте ваш код тут

        # очередь заполнена
        if self.length == self.size:
            raise OverflowError
        
        # если крайняя справа ячейка заполнена,
        # переносим индекс последнего элемента в начало
        if self.last == self.size - 1:
            self.last = -1

        # если массив пуст, первый элемент встанет на индекс 0
        if self.length == 0:
            self.first = 0
        
        # увеличиваем индекс последнего элемента на 1
        self.last += 1
        
        # вставляем новый элемент
        self.data[self.last] = value

        # увеличиваем длину очереди на 1
        self.length += 1

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        # Добавьте ваш код тут

        # если массив пуст, возвращаем None
        if self.length == 0:
            return
        
        # находим удаляемый элемент (первый в очереди)
        elem = self.data[self.first]

        # если первый элемент стоит в крайней справа ячейке,
        # новый первый элемент будет иметь индекс 0
        if self.first == self.size - 1:
            self.first = 0
        # иначе индекс первого элемента сдвинется вправо
        else:
            self.first += 1

        # уменьшаем длину на 1
        self.length -= 1

        # возвращаем удаляемый элемент
        return elem
    
queue = Queue(3)
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
# queue.enqueue(8) - OverflowError

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())
