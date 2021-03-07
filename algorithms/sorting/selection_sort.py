def selection_sort(input_list=[]):
    """
    O(n^2)
    :param input_list:
    :return: ascending list
    """
    size = len(input_list)
    operation_counter = 0
    for index in range(size):
        min_index = index
        for index2 in range(index + 1, size):
            operation_counter += 1
            if input_list[index2] < input_list[min_index]:
                min_index = index2
        input_list[index], input_list[min_index] = input_list[min_index], input_list[index]
    print('Operation counter : {}'.format(operation_counter))


if __name__ == '__main__':
    l1 = [6, 5, 3, 1, 8, 7, 2, 4]
    l2 = []
    l3 = [1]
    selection_sort(l1)
    selection_sort(l2)
    selection_sort(l3)
    print(l1)
    print(l2)
    print(l3)
