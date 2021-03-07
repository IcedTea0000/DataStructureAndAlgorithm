graph = {"A": ["B", "D", "C"],
         "B": ["E"],
         "C": ["G", "F"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"]}


def dfs_non_recursive(graph, start_node):
    if start_node is None or start_node not in graph:
        return "Invalid input"
    path = []
    stack = [start_node]
    while (len(stack) != 0):
        s = stack.pop()
        print('traversing through {}'.format(s))
        if s not in path:
            path.append(s)
        if s not in graph:
            # leaf node
            print('{} not in graph'.format(s))
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)
    return " ".join(path)


graph2 = {"A": ["B", "D", "C"],
          "B": ["E"],
          "C": ["G", "F"],
          "D": ["H"],
          "E": ["I"],
          "F": ["J"],
          "G": [],
          "H": [],
          "I": [],
          "J": []}


def dfs_non_recursive2(graph, start_node):
    stack = []
    path = []
    stack.append(start_node)
    while stack:
        current_node = stack.pop()
        if current_node not in path:
            path.append(current_node)
        if not graph[current_node]:
            continue
        for connector in graph[current_node]:
            stack.append(connector)
    return path


# print(dfs_non_recursive(graph, 'A'))
print(dfs_non_recursive2(graph2, 'A'))
