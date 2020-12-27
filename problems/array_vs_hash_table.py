# input: unsorted array [1,2,1,2,5,6,7,8]
# output: first character that appear again = 1

# input: []
# output: None

# input [1,2,3]
# output: None
import unittest


def get_first_recurring_character1(input_list=[]):
    """
    O(n^2)
    brute force approach
    :param input_list: unsorted list
    :return: first recurring character
    """
    for index_to_compare in range(len(input_list)):
        for index_comparing in range(index_to_compare + 1, len(input_list)):
            if input_list[index_to_compare] == input_list[index_comparing]:
                return input_list[index_to_compare]
    return None


def get_first_recurring_character2(input_list=[]):
    """
    O(n)
    :param input_list: unsorted list
    :return: first recurring character
    """
    dict_temp = dict()
    for element in input_list:
        if dict_temp.get(element) is not None:
            return element
        else:
            dict_temp.update({element: True})
    return None


class TestLocalMethods(unittest.TestCase):
    def test_empty_list(self):
        input_list = []
        result = get_first_recurring_character1(input_list)
        expect = None
        self.assertEqual(result, expect)

    def test_no_recurring_list(self):
        input_list = [1, 2, 3, 4, 5]
        result = get_first_recurring_character1(input_list)
        expect = None
        self.assertEqual(result, expect)

    def test_recurring_list1(self):
        input_list = [1, 2, 1, 2, 2, 2, 4, 5, 6]
        result = get_first_recurring_character1(input_list)
        expect = 1
        self.assertEqual(result, expect)

    def test_recurring_list2(self):
        input_list = [1, 2, 2, 1, 3, 4, 5]
        result = get_first_recurring_character1(input_list)
        expect = 2
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
