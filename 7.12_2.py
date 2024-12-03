def char_decorator(tag="h1"):
    def make_tag(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper

    return make_tag


@char_decorator("div")
def get_low(s_inp):
    """Make upper char become lower
       !!!Works only for English chars!!!"""
    res = [chr(ord(i) + 32) if ord(i) in range(65, 97) else i for i in s_inp]
    return "".join(res)


print(get_low("HEllo WorlD"))
