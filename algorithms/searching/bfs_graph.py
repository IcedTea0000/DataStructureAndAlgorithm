graph = {"A": ["B", "D", "C"],
         "B": ["E"],
         "C": ["G", "F"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"],
         "G": [],
         "H": [],
         "I": [],
         "J": []}


def bfs_non_recursive(graph, starting_node):
    queue = [starting_node]
    path = []
    while queue:
        pointer_node = queue.pop(0)
        if pointer_node not in path:
            path.append(pointer_node)
        for connector in graph[pointer_node]:
            queue.append(connector)
        print('Current queue: {}'.format(queue))
    return path


print(bfs_non_recursive(graph, 'A'))
