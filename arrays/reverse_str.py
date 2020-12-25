def reverse(string=''):
    """

    :param string: input text
    :return: reverse text of input text
    """
    # check input

    result_list = []
    for index in range(len(string) - 1, -1, -1):
        result_list.append(string[index])
    reversed_string = ''.join(result_list)
    return reversed_string


print(reverse('Hi this is Martin'))
