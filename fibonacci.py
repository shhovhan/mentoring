def fibonacci(n):
    """
    Function which returns first n fibonacci numbers
    :param n: qty of numbers
    :return: array of first n fibonacci numbers
    """
    fib = [1, 1]
    if n > 2:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])

    return fib


print(fibonacci(100))
