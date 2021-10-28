def hi(func):
    def wrapper(*args, **kwargs):
        str = "hello " + func(*args, **kwargs)
        return str

    return wrapper


def hello(name):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            return 'Hello ' + func(*args, **kwargs) + ' and ' + name
        return inner_wrapper

    return wrapper


@hello('Hanna')
def greeting(name):
    return name


print(greeting('Shushan'))
