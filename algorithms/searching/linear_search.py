def my_linear_search(input_list, number):
    """
    :param input_list:
    :param number:
    :return: index of first appearance, if not return -1
    """
    size = len(input_list)
    for index in range(size):
        if input_list[index] == number:
            return index
    return -1


if __name__ == '__main__':
    l1 = [43, 234, 1, 23, 44, 5798, 4, 2, 0]
    print(my_linear_search(l1, 0))
    print(my_linear_search(l1, -45))
