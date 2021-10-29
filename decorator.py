def milk_coffee(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('+Milk')
    return wrapper


def syrup(syrup_type):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'+{syrup_type} syrup')
        return inner_wrapper
    return wrapper


def sugar(how_many):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(f'+Sugar {how_many} spoons')
        return inner_wrapper
    return wrapper


def type_of_coffee(name):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f'Make {name}')
            func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@sugar(2)
@syrup('mapple')
@milk_coffee
def coffee(type_of_coffee):
    print(f'Making {type_of_coffee}')
    print('Coffee')


coffee('Cappuccino')
