class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return 'Data: {} \nNode address: {}\nNext node address: {}\n'.format(self.data, repr(self),
                                                                             repr(self.next_node))

    def set_data(self, data=None):
        self.data = data

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node


class MyQueueLinkedList:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def __str__(self):
        return 'Size : {}\n Top : {}\n Bottom : {}\n'.format(self.size, self.top, self.bottom)

    def peek(self):
        pass

    def enqueue(self, value):
        """
        add value to the top of queue
        :param value:
        :return:
        """
        new_node = Node(data=value)
        if self.top is None:
            self.top = new_node
            self.bottom = self.top
        else:
            self.bottom.set_next_node(new_next_node=new_node)
            self.bottom = new_node
        self.size += 1

    def dequeue(self):
        """
        get bottom value from queue, remove that node from queue
        :return: bottom value of queue
        """
        top_node = self.top
        if top_node is self.bottom:
            self.bottom = None
        if top_node is None:
            return None
        else:
            top_node_value = top_node.get_data()
            self.top = top_node.get_next_node()
            del top_node
            self.size -= 1
            return top_node_value
        pass


if __name__ == '__main__':
    my_queue = MyQueueLinkedList()
    my_queue.enqueue(value=10)
    my_queue.enqueue(value=20)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())

    print(my_queue)
