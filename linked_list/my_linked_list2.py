class Node:
    def __init__(self, data=None, next_node_reference=None):
        self.data = data
        self.next_node_reference = next_node_reference

    def __str__(self):
        return 'Data: {}\nCurrent Node Address: {}\nNext Node Address: {}'.format(self.data, repr(self),
                                                                                  repr(self.next_node_reference))

    def set_data(self, new_data=None):
        self.data = new_data

    def set_next_node_reference(self, next_node_reference=None):
        self.next_node_reference = next_node_reference

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node_reference


class MySinglyLinkedList:
    def __init__(self, data):
        self.head = Node(data=data)
        self.tail = self.head

    def __str__(self):
        return 'Head: {}\nTail: {}\n'.format(self.head, self.tail)

    def append(self):
        pass

    def prepend(self):
        pass

    def get_node(self, index=None):
        return
        pass

    def insert_node(self, index=None, new_node=None):
        pass

    def remove_node(self, index=None):
        pass

    pass


if __name__ == '__main__':
    # my_node = Node(data=10)
    # print(my_node)
    my_singly_linked_list = MySinglyLinkedList(10)
    print(my_singly_linked_list)
