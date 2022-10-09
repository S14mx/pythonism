from functools import wraps


def add_itself(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        og_val = func(*args, **kwargs)
        return og_val + og_val

    return wrapper


def square_itself(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        og_val = func(*args, **kwargs)
        return og_val ** 2

    return wrapper


def multiply_by_three(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        og_val = func(*args, **kwargs)
        return og_val * 3

    return wrapper


@square_itself
@add_itself
def take_number(number):
    return number


def add_numbers(*args, **kwargs):
    _sum = 0
    if args:
        for num in args:
            _sum += num
        return _sum
    if kwargs:
        for key, value in kwargs.items():
            for num in value:
                _sum += num
        return _sum
