def insertion_sort(input_list=[]):
    """
    O(n^2)
    :param input_list:
    :return: ascending list
    """
    size = len(input_list)
    for index in range(1, size):
        current_value = input_list[index]
        current_index = index
        while (current_index != 0) and (input_list[current_index - 1] > current_value):
            input_list[current_index] = input_list[current_index - 1]
            current_index -= 1
        input_list[current_index] = current_value


l1 = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
insertion_sort(l1)
print(l1)
