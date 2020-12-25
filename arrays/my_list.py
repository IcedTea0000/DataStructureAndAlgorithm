"""
my implementation of list
"""


class MyList():
    def __init__(self):
        self.length = 0
        self.data = []

    def __str__(self):
        return 'length: {}\ndata: {}'.format(self.length, self.data)

    def get(self, index):
        """
        O(1) -> O(c)
        :param index: pointer to list
        :return: value of object at pointer
        """
        return self.data[index]

    def push(self, element):
        """
        O(2) -> O(c)
        add item to the end of list
        :param element: object to add to list
        """
        self.data.append(element)
        self.length += 1

    def pop(self):
        """
        O(4) -> O(c)
        return last item of list and delete from list
        :return: last item
        """
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        """
        O(3) -> O(c)
        delete item at index in list
        :param index: index of item want to delete
        :return: item at index in list
        """
        delete_item = self.data[index]
        self.lshift_items(index)
        return delete_item

    def lshift_items(self, index):
        """
        O(n+2) -> O(n)
        shift all items of list to left 1 index
        :param index: position to start shifting to left
        :return:
        """
        for index2 in range(index, self.length - 1):
            self.data[index2] = self.data[index2 + 1]
        del self.data[self.length - 1]
        self.length -= 1


if __name__ == '__main__':
    l1 = MyList()
    l1.push('test1')
    l1.push('test2')
    l1.push('test3')
    l1.push('test4')
    # last_item = l1.pop()
    # print('last item: {}'.format(last_item))
    l1.delete(1)
    print(l1)
