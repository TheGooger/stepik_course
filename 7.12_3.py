t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def string_decorator(chars="!?"):
    def remove_chars(func):
        def wrapper(*args, **kwargs):
            res = "".join(i if i not in chars else "-" for i in func(*args, **kwargs))
            while "--" in res:
                res = res.replace("--", "-")
            return res

        return wrapper

    return remove_chars


@string_decorator("!?:;., ")
def make_lat(s_inp):
    return "".join([t.get(i, i) for i in s_inp.lower()])


print(make_lat("Декораторы - это круто!"))
