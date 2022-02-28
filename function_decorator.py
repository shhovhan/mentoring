import functools
import time
# decorator function to add milk in coffee
def milk_coffee(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('+Milk')
    return wrapper


# decorator function to add syrup in coffee. Accepts type of syrup as an argument
def syrup(syrup_type):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'+{syrup_type} syrup')
        return inner_wrapper
    return wrapper


# decorator function to add sugar in coffee. Accepts qty of added sugar as an argument
def sugar(how_many):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'+Sugar {how_many} spoons')
        return inner_wrapper
    return wrapper


# decorator function to mention type coffee. Accepts type as an argument
def type_of_coffee(name):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f'Make {name}')
            func(*args, **kwargs)
        return inner_wrapper
    return wrapper


# decorator function to calculate function calls
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls_count += 1
        func(*args, **kwargs)

    wrapper.calls_count = 0
    return wrapper


def timing(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f'Finished {func.__name__} in {run_time} secs')
        return value
    return wrapper


def debug(func):
    """Print the function arguments and return value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with arguments {args, kwargs}')
        return func(*args, **kwargs)
    return wrapper