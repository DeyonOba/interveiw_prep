#!/usr/bin/python3
"""
Script impliments the Mathematical Factorial equation using iteration
and recursive processes.

A factorial, in mathematics is the production of all positive integers
less than or equal to a given positive integer and denoted by that
integer and an exclamation point.

n! = (n - 0) * (n - 1) * (n - 2) * ... * 3 * 2 * 1

Example
-------
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(3)
3
>>> factorial(4)
24

Raises
------
    TypeError: For non integer type.
    ValueError: For negative integers.
"""

def factorial(n: int) -> int:
    """
    Factorial function using iteration method.

    Alogrithm implementation:
    1. Function only accepts positive integer, else raise exception.
    2. Create a variable `result` and assign the integer 1 to it. `result` is assign 1 because factorial of 0,
    the first possible integer is equal to 1.
    >>> factorial(0)
    1
    3. Iterate through n, with a range stating from 2 to n. The number 1 is skip since the factorial of 1 is also 1.
    4. Within the loop multiple each integer withing the range by the integer stored in `result`.
    5. Finally return the integer stored in `result` after the iteration operation has been completed.
    """
    if type(n) is not int:
        raise TypeError(f"Function accepts only integers.")
    elif n < 0:
        raise ValueError(f"Negative integer {n} not accepted.")
    
    result = 1
    for num in range(2, n + 1):
        result *= num

    return result


def recursive_factorial(n: int) -> int:
    """
    Factorial function using recursive method.

    Algorithm diagramatic explaination:

    call functions
    `recursive_factorial(3)`
        First function call
        1. if type(n) is not int -> False
        2. else if n < 0 -> 3 is less than 0 -> False
        3. Is 3 equal to 0 -> False
        4. Then n * `recursive_factorial(n - 1)`
            Second function call
                `3 * recursive_factorial(3 - 1)`
            5. n is now equal to 2 -> n = 2
            6. if  type(n) is not int -> False
            7. else if n < 0 -> 2 is less than 0 -> False
            8. Is 2 equal to 0 -> False
            9. Then n * `recursive_factorial(n - 1)`
                Third function call
                    `3 * 2 * recursive_function(2 - 1)`
                10. n is now equal to 1 -> n = 1
                11. if  type(n) is not int -> False
                12. else if n < 0 -> 1 is less than 0 -> False
                13. Is 1 equal to 0 -> False
                14. Then n * `recursive_factorial(n - 1)`
                    Fourth function call
                    `3 * 2 * 1 * recursive_factorial(n - 1)`
                    15. n is now equal to 0 -> n = 0
                    16. if  type(n) is not int -> False
                    17. else if n < 0 -> 2 is less than 0 -> False
                    18. Is 0 equal to 0 -> True
        19. Finall return 3 * 2 * 1 * 1
        OUTPUT -> 6
    """
    if type(n) is not int:
        raise TypeError(f"Function accepts only integers.")
    elif n < 0:
        raise ValueError(f"Negative integer {n} not accepted.")

    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1) 
