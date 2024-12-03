from functools import wraps


str_inp = "1 2 3"


def sum_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))

    return wrapper


@sum_decorator
def get_list(data):
    """Функция для формирования списка целых значений"""
    return [int(i) for i in data.split()]


print(get_list.__name__)
print(get_list.__doc__)
