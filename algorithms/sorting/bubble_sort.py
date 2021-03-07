def bubble_sort_not_optimized(input_list=[]):
    """
    O(n^2)
    :param input_list:
    :return: ascending list
    """
    operation_counter = 0
    size = len(input_list)
    for index1 in range(size - 1):
        for index2 in range(size - 1):
            if input_list[index2] > input_list[index2 + 1]:
                input_list[index2], input_list[index2 + 1] = input_list[index2 + 1], input_list[index2]
            operation_counter += 1
    print('operation_counter : {}'.format(operation_counter))


def bubble_sort_optimized(input_list=[]):
    """
    O(n^2)
    :param input_list:
    :return:
    """
    last_swap = True
    operation_counter = 0
    size = len(input_list)
    while last_swap:
        last_swap = False
        for index in range(size - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                last_swap = True
            operation_counter += 1
    print('operation_counter : {}'.format(operation_counter))


if __name__ == '__main__':
    l1 = [6, 5, 3, 1, 8, 7, 2, 4]
    l2 = []
    l3 = [1]
    bubble_sort_not_optimized(l1)
    bubble_sort_optimized(l1)
    print(l1)
