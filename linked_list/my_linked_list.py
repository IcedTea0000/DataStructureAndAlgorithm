class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return '[Data: {} \nNext_node: {}]'.format(self.data, self.next_node)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class MyLinkedList():
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def __str__(self):
        return '{}'.format(self.head)

    def append(self, data):
        new_node = Node(data=data)
        self.tail.set_next_node(new_node)
        self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data=data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.size += 1

    def insert(self, index, data):
        previous_node = self.head
        current_node = self.head
        new_node = Node(data)
        if index >= self.size:
            my_linked_list.append(data)
        elif index <= 0:
            my_linked_list.prepend(data)
        else:
            previous_node = my_linked_list.get_node(index - 1)
            new_node.set_next_node(new_next_node=previous_node.get_next())
            previous_node.set_next_node(new_node)
            self.size += 1

    def get_node(self, index):
        counter = 0
        if index < 0:
            index = 0
        current_node = self.head
        while (counter != index) and (current_node.get_next() is not None):
            current_node = current_node.get_next()
            counter += 1
        return current_node

    def remove(self, index):
        if index <= 0:
            new_node = self.head.get_next()
            self.head = Node(data=new_node.get_data(), next_node=new_node.get_next())
            del new_node
        elif index >= self.size:
            previous_node = self.get_node(self.size - 2)
            previous_node.set_next_node(None)
        else:
            previous_node = self.get_node(index - 1)
            node_to_delete = previous_node.get_next()
            previous_node.set_next_node(node_to_delete.get_next())
        self.size -= 1

        pass


if __name__ == '__main__':
    my_linked_list = MyLinkedList(10)
    # print(my_linked_list)
    my_linked_list.append(20)
    my_linked_list.prepend(5)
    my_linked_list.insert(index=1, data=6)
    my_linked_list.insert(index=0, data=4)
    print(my_linked_list)
    print('\n')
    my_linked_list.remove(9)
    print(my_linked_list)
