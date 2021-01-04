class MyGraph:
    def __init__(self):
        self.number_of_nodes = 0
        self.node_list = []
        self.adjacent_list = [
            # format
            # index 0: [false, true, true]
            # index 1: [true, false, false]
            # index 2: [false, false, true]
        ]

    def add_vertex(self, node):
        # add new node to graph
        # there must no duplicate node in Graph
        self.node_list.append(node)
        for connections in self.adjacent_list:
            connections.append(False)
        self.adjacent_list.append([])
        self.number_of_nodes += 1
        for index in range(self.number_of_nodes):
            self.adjacent_list[self.number_of_nodes - 1].append(False)
        pass

    def add_edge(self, node1, node2):
        # undirected graph only
        for index in range(self.number_of_nodes):
            if node1 == self.node_list[index]:
                index_node_1 = index
            if node2 == self.node_list[index]:
                index_node_2 = index

        self.adjacent_list[index_node_1][index_node_2] = True
        self.adjacent_list[index_node_2][index_node_1] = True

    def get_connections(self):
        "output format: connected vertex: [1,2], [3,4,5]"
        visited_nodes = []
        result = []
        for index in range(self.number_of_nodes):
            visited_nodes.append(False)

        for index in range(self.number_of_nodes):
            if visited_nodes[index] == False:
                temp = []
                result.append(self.DFSUtil(temp, index, visited_nodes))

        return result

    def DFSUtil(self, temp, index, visited_nodes):
        # Mark the current vertex as visited
        visited_nodes[index] = True

        # Store the vertex to list
        temp.append(self.node_list[index])

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in range(self.number_of_nodes):
            if (self.adjacent_list[index][i]) and (not visited_nodes[i]):
                # Update the list
                temp = self.DFSUtil(temp, i, visited_nodes)
        return temp


if __name__ == '__main__':
    my_graph = MyGraph()
    my_graph.add_vertex(1)
    my_graph.add_vertex(2)
    my_graph.add_vertex(3)
    my_graph.add_vertex(4)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(1, 2)

    print(my_graph.adjacent_list)

    print(my_graph.get_connections())
