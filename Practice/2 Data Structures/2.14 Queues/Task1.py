class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    """
    Очередь на базе двунаправленного связного списка.
    """

    def __init__(self):
        self.top = Node(None)
        self.first = None

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        # Добавьте ваш код тут
        elem = Node(value)

        if self.first:
            self.top.next_node.prev_node, elem.next_node = elem, self.top.next_node
        else:
            self.first = elem
            
        self.top.next_node = elem
        elem.prev_node = self.top

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        # Добавьте ваш код тут
        elem = self.first

        if elem is None:
            return
        
        elem.prev_node.next_node = None

        if self.top.next_node is None:
            self.first = None
        else:
            self.first = elem.prev_node
            
        return elem.value

queue = Queue()
queue.enqueue(12)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(8)
print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())
