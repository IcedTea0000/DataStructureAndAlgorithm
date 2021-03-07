# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811...
calculation_counter = 0
calculation_counter2 = 0


def cal_fibonacci_no_cache(index):
    global calculation_counter
    calculation_counter += 1
    if index < 2:
        return 1
    else:
        return cal_fibonacci_no_cache(index - 1) + cal_fibonacci_no_cache(index - 2)


def cal_fibonacci_cache(index):
    cache = {}

    def cal_fibonacci(index2):
        global calculation_counter2
        calculation_counter2 += 1
        if index2 in cache:
            return cache[index2]
        else:
            if index2 < 2:
                return index2
            else:
                cache[index2] = cal_fibonacci(index2 - 1) + cal_fibonacci(index2 - 2)
                return cache[index2]

    return cal_fibonacci(index)


# print(cal_fibonacci_no_cache(10))
# print('Calculation counter : {}'.format(calculation_counter))
# print(cal_fibonacci_cache(50))
# print('Calculation counter 2 : {}'.format(calculation_counter2))
def cal_factorial_no_cache(number):
    global calculation_counter
    calculation_counter += 1
    if number == 1:
        return number
    else:
        return number * cal_factorial_no_cache(number - 1)


cache = {}


def cal_factorial_cache(number):
    global cache

    def cal_factorial(n):
        global calculation_counter2
        calculation_counter2 += 1
        if n in cache:
            return cache[n]
        else:
            if n == 1:
                return number
            else:
                cache[n] = number * cal_factorial_cache(number - 1)
                return cache[n]

    return cal_factorial(number)


# print(cal_factorial_no_cache(10))
# print(cal_factorial_no_cache(10))
# print('Calculation counter : {}'.format(calculation_counter))
print(cal_factorial_cache(10))
print(cal_factorial_cache(10))
print('Calculation counter : {}'.format(calculation_counter2))
