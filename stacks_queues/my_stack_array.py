class MyStackArray:
    def __init__(self, value=None):
        self.data = []
        if value is None:
            self.size = 0
        else:
            self.size = 1

    def __str__(self):
        return 'Size: {}\n Data: {}'.format(self.size, self.data)

    def peek(self):
        """
        view the top element
        :return:
        """
        return self.data[0]

    def push(self, value):
        """
        add data to the top of stack
        :param data:
        :return:
        """
        self.data.append(value)
        self.size += 1

    def pop(self):
        """
        return element on top of stack and remove out of stack
        :return:
        """
        if self.size == 0:
            return None
        top_value = self.data[self.size - 1]
        del self.data[self.size - 1]
        self.size -= 1
        return top_value

    def is_empty(self):
        """
        True/False if the stack is empty
        :return:
        """
        return self.size == 0


if __name__ == '__main__':
    my_stack = MyStackArray()

    print(my_stack.pop())
    print(my_stack.is_empty())
