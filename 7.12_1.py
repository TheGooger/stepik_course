s_inp = "5 6 3 6 -4 6 -1"


def sum_decorator(start=0):
    def sum_add(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start

        return wrapper

    return sum_add


@sum_decorator(start=5)
def get_sum(data):
    return sum([int(i) for i in data.split()])


print(get_sum(s_inp))
