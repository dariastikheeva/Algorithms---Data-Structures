class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.head = None
        self.len_list = 0

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.len_list += 1
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)
        self.len_list += 1

    def length(self):
        # Добавьте ваш код тут.
        return self.len_list
    
lst = List()
print(lst.length())

lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
print(lst.length())