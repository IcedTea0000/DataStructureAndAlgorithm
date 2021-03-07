class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.address = repr(self)

    def __str__(self):
        return 'Data: {}\n Current node: {}\n Left node: {}\n Right node: {}\n'.format(self.data, self.address,
                                                                                       repr(self.left_node),
                                                                                       repr(self.right_node))

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data

    def set_left_node(self, node):
        self.left_node = node

    def set_right_node(self, node):
        self.right_node = node

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def get_data(self):
        return self.data


class MyBinarySearchTree:
    def __init__(self, data=None):
        self.root_node = Node(data)
        if data is None:
            self.size = 0
        else:
            self.size = 1

    def __str__(self):
        return 'Size : {}\n Root node: {}'.format(self.size, self.root_node)

    def insert_batch(self, input_list=[]):
        for value in input_list:
            self.insert(data=value)

    def insert(self, data):
        if data is None:
            return
        new_node = Node(data=data)
        # if tree is empty
        if not self.root_node.data:
            self.root_node = new_node
        else:
            pointer_node = self.root_node
            while True:
                # traverse right
                if new_node > pointer_node:
                    if not pointer_node.get_right_node():
                        pointer_node.set_right_node(new_node)
                        break
                    else:
                        pointer_node = pointer_node.get_right_node()
                # traverse left
                elif new_node < pointer_node:
                    if not pointer_node.get_left_node():
                        pointer_node.set_left_node(new_node)
                        break
                    else:
                        pointer_node = pointer_node.get_left_node()
                else:
                    # data existed in tree
                    return
        self.size += 1

    def lookup(self, data):
        # traverse tree
        node_to_compare = Node(data=data)
        pointer_node = self.root_node
        counter = 0
        while not pointer_node:
            counter += 1
            if pointer_node == node_to_compare:
                print('Node traveled : {}'.format(counter))
                return pointer_node
            elif node_to_compare > pointer_node:
                pointer_node = pointer_node.get_right_node()
            else:
                pointer_node = pointer_node.get_left_node()
        # not found
        return None

    def remove(self, data):
        pass

    def my_bfs(self):
        """
        tree nodes will be added to a queue by layer from root node
        if node exist left/right nodes, add to queue while extracting data from nodes in queue to a list
        :return:
        """
        current_node = self.data
        list_values = []
        queue_temp = []
        queue_temp.append(current_node)
        while (len(queue_temp) > 0):
            current_node = queue_temp.pop(0)
            list_values.append(current_node.value)
            if current_node.left:
                queue_temp.append(current_node.left)
            if current_node.right:
                queue_temp.append(current_node.right)
        return list_values

    def my_bfs_recursive(self, queue_temp=[], list_values=[]):
        if len(queue_temp) <= 0:
            return list_values
        current_node = queue_temp.pop
        list_values.append(current_node.value)
        if current_node.left:
            queue_temp.append(current_node.left)
        if current_node.right:
            queue_temp.append(current_node.right)
        return self.my_bfs_recursive(queue_temp, list_values)


if __name__ == '__main__':
    my_tree = MyBinarySearchTree()
    my_tree.insert(data=50)
    my_tree.insert(data=40)
    my_tree.insert(data=60)
    # print(my_tree)
    my_tree.insert_batch(input_list=[1, 2, 5, 5, 6, 60, 80, 100])
    # print(my_tree)
    # print(my_tree.lookup(data=100))
    print(my_tree.my_bfs())
