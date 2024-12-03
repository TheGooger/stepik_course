s_1 = "house river tree car"
s_2 = "дом река дерево машина"


def tuple_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        t_dict = {res[0][i]: res[1][i] for i in range(len(res[1]))}
        return t_dict
    return wrapper


@tuple_decorator
def get_tuple(a, b):
    return a.split(), b.split()


d = get_tuple(s_1, s_2)
print(*sorted(d.items()))
