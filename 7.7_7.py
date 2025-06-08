n = 5

def get_path(n):
    if n == 1:
        return n
    elif n == 2:
        return n
    return get_path(n-1) + get_path(n-2)