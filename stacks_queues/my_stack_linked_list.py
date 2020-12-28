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


class MyStackLinkedList:
    def __init__(self, data):
        self.top = Node(data=data)
        self.bottom = self.top
        self.size = 1

    def __str__(self):
        return 'Size : {}\n Top node: {}\n Bottom node: {}'.format(self.size, self.top, self.bottom)

    def peek(self):
        """
        view the top element
        :return: top element of stack
        """
        return self.top.data

    def push(self, data):
        """
        add data to the top of stack (in this implementation == prepend)
        :param data: new data add to top of stack
        :return:
        """
        new_node = Node(data=data, next_node=self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        """
        return element on top of stack and remove out of stack
        :return: element on top of stack and remove out of stack
        """
        top_node = self.top
        if self.size == 0:
            self.bottom = None
        if top_node is None:
            return None
        else:
            self.top = self.top.get_next_node()
            self.size -= 1
        return top_node.data

    def is_empty(self):
        """
        True/False if the stack is empty
        :return:
        """
        return self.bottom is None


if __name__ == '__main__':
    my_stack = MyStackLinkedList(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)

    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())

    print(my_stack)
