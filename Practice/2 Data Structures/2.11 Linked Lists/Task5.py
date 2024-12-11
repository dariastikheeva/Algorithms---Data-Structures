class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.top = Node(None)

    def append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        """

        # Перебираем поочереди все элементы, чтобы найти последний
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(value)

    def insert(self, value, after_value):
        """
        Вставка нового элемента в середину связного списка.
        После значения after_value
        """

        # Добавьте ваш код тут
        current = self.top.next_node

        while current is not None:
            if current.value == after_value:
                new_node = Node(value)
                current.next_node, new_node.next_node = new_node, current.next_node
            
            current = current.next_node

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"