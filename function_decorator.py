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
