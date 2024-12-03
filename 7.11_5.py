t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

inp_s = "Python - это круто!"


def string_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        while "--" in res:
            res = res.replace("--", "-")
        return res
    return wrapper


@string_decorator
def get_lat(s):
    res = ""
    for i in s.lower():
        if i in " :;.,_":
            res += "-"
        elif i in t.keys():
            res += t[i]
        else:
            res += i
    return res


print(get_lat(inp_s))
