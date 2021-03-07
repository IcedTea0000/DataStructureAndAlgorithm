def find_factorial_recursive(number):
    if number > 1:
        return number * find_factorial_recursive(number - 1)
    else:
        return 1


def find_factorial_iterator(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

# print(find_factorial_recursive(2))
# print(find_factorial_iterator(2))
