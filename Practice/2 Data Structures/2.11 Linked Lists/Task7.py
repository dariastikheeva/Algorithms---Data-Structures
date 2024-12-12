class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def __str__(self):
        return str(self.value)


class List:
    """
    Двунаправленный связный список.
    """

    def __init__(self):

        # Ограничитель
        self.top = Node()

    def append(self, value):
        """
        Добавление нового элемента в конец двунаправленного списка.
        Время работы O(N).
        """

        # Находим последнюю ячейку.
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Вставляем новую ячеку после current и делаем обратную ссылку.
        new_node = Node(value)
        current.next_node = new_node
        new_node.prev_node = current

    def remove(self, value):
        """
        Удаление элемента из двунаправленного списка.
        """
        # Добавьте ваш код тут.
        current = self.top.next_node

        while current:
            if current.value == value:
                break

            current = current.next_node

        if current.next_node:
            current.next_node.prev_node = current.prev_node

        current.prev_node.next_node = current.next_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
    
lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(5)
lst.append(7)
print(lst)

lst.remove(3)
lst.remove(7)
print(lst)

five = lst.top.next_node.next_node.next_node
print(five.prev_node)