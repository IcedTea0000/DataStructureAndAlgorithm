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

    # example 3 types of dfs:
    # tree:
    #     101
    # 33      105
    # in order: 33,101, 105
    # pre order: 101, 33, 105
    # post order: 33, 105, 101
    def dsf_in_order(self):
        return self.traverse_in_order(self.root_node, [])

    def traverse_in_order(self, node, list_data):
        if node.left_node:
            self.traverse_in_order(node.left_node, list_data)
        list_data.append(node.data)
        if node.right_node:
            self.traverse_in_order(node.right_node, list_data)
        return list_data

    def dsf_pre_order(self):
        return self.traverse_pre_order(self.root_node, [])

    def traverse_pre_order(self, node, list_data):
        list_data.append(node.data)
        if node.left_node:
            self.traverse_pre_order(node.left_node, list_data)
        if node.right_node:
            self.traverse_pre_order(node.right_node, list_data)
        return list_data

    def dsf_post_order(self):
        return self.traverse_post_order(self.root_node, [])

    def traverse_post_order(self, node, list_data):
        if node.left_node:
            self.traverse_post_order(node.left_node, list_data)
        if node.right_node:
            self.traverse_post_order(node.right_node, list_data)
        list_data.append(node.data)
        return list_data


if __name__ == '__main__':
    my_tree = MyBinarySearchTree()
    my_tree.insert(data=50)
    my_tree.insert(data=40)
    my_tree.insert(data=60)
    my_tree.insert(data=35)
    my_tree.insert(data=41)
    my_tree.insert(data=63)
    # print(my_tree)
    # my_tree.insert_batch(input_list=[70, 45, 35, 28, 37, 30, 59])
    # print(my_tree)
    # print(my_tree.lookup(data=100))
    print(my_tree.dsf_in_order())
    print(my_tree.dsf_pre_order())
    print(my_tree.dsf_post_order())
