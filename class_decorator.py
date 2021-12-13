from functools import wraps


class MilkCoffee:
    """ Class decorator equivalent of milk_coffee function decorator."""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        print('+Milk')


class Syrup:
    """ Class decorator equivalent of syrup function decorator."""
    def __init__(self, syrup_type):
        self.syrup_type = syrup_type

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """wrapper docstring"""
            func(*args, **kwargs)
            print(f'+{self.syrup_type} syrup')
        return wrapper


class Sugar:
    """ Class decorator equivalent of sugar function decorator."""
    def __init__(self, qty):
        self.qty = qty

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'+Sugar {self.qty} spoons')
        return wrapper


class CountCalls:
    """ Class decorator equivalent of count_calls function decorator."""
    def __init__(self, func):
        self.func = func
        self.calls_count = 0

    def __call__(self, *args, **kwargs):
        self.calls_count += 1
        self.func(*args, **kwargs)

