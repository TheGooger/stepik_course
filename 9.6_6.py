lst_in = [
    'смартфон:120000', 'яблоко:2', 'сумка:560',
    'брюки:2500', 'линейка:10', 'бумага:500'
]

d = dict((int(i.split(':')[1]), i.split(':')[0]) for i in lst_in)
# d = dict(i.split(':')[::-1] for i in lst_in)


def get_cheap(d):
    return [d[i] for i in sorted(d)][:3]


print(*get_cheap(d))
