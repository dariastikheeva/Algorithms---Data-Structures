class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Добавьте ваш код тут.
        if self.top.next_node is None:
            return
        elem = self.top.next_node
        self.top.next_node = elem.next_node
        return elem.value

    def push(self, value):
        """
        Добавляет элемент со значением value в стек.
        """
        # Добавьте ваш код тут.
        elem = Node(value)
        self.top.next_node, elem.next_node = elem, self.top.next_node
