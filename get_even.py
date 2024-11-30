def get_even(*args):
    return [i for i in args if i % 2 == 0]


print(get_even(1, 2, 3, 4, 5, 6))