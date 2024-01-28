import math
from functools import reduce
from operator import mul


def factorial_math(number_input: int) -> int:
    """
    Calculate the factorial of a given number using the math.factorial function.

    Args:
        number_input (int): The number for which factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    return math.factorial(number_input)


def factorial_recursive(number_input: int) -> int:
    """
    Calculate the factorial of a given number using a recursive approach.

    Args:
        number_input (int): The number for which factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if number_input == 0:
        return 1
    else:
        return number_input * factorial_recursive(number_input - 1)


def factorial_reduce(number_input: int) -> int:
    """
    Calculate the factorial of a given number using the reduce function.

    Args:
        number_input (int): The number for which factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    return reduce(mul, range(1, number_input + 1), 1)


def factorial_while(number_input: int) -> int:
    """
    Calculate the factorial of a given number using a while loop.

    Args:
        number_input (int): The number for which factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    result = 1
    while number_input > 0:
        result *= number_input
        number_input -= 1
    return result


def factorial_iterative(number_input: int) -> int:
    """
    Calculate the factorial of a given number using an iterative approach.

    Args:
        number_input (int): The number for which factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    result = 1
    for i in range(1, number_input + 1):
        result *= i
    return result


if __name__ == '__main__':
    try:
        number = int(input("enter a number to get its factorial: "))
        print(factorial_reduce(number))
        print(factorial_while(number))
        print(factorial_math(number))
        print(factorial_recursive(number))
        print(factorial_iterative(number))
    except Exception as e:
        print(e)
