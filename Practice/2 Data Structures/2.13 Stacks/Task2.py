class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class Stack:
    """
    Стек на базе связного списка.
    """
    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Получаем верхний элемент
        top = self.top.next_node

        # Перестраиваем связи и возвращаем значение
        if top:
            self.top.next_node = top.next_node
            return top.value

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        # Добавляем элемент в начало связного списка
        new_node = Node(value)

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node

    def clear(self):
        """
        Очищает стек.
        """
        # Добавьте ваш код тут.
        self.top.next_node = None

    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        # Добавьте ваш код тут.
        return self.top.next_node.value if self.top.next_node else None

    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        # Добавьте ваш код тут.
        n = 0
        current = self.top.next_node

        while current:
            n += 1
            current = current.next_node
            
        return n


stack = Stack()
stack.push(12)
stack.push(7)
stack.push(6)
print(stack.peek())

print(stack.count())

stack.clear()
print(stack.count())

print(stack.peek())
