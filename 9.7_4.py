lst_in = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да',
          '2;Арамис;3;Да', '3;Атос;4;Да',
          '4;д\'Артаньян;2;Нет', '5;Балакирев;1;Нет']

# t = tuple(tuple(i.split(';')) for i in lst_in)
t = ()
for row in lst_in:
    temp = []
    for val in row.split(';'):
        if len(val) == 1:
            temp.append(int(val))
        else:
            temp.append(val)
    t += tuple(temp),
d = {1: 0, 3: 1, 2: 2, 0: 3}
print(t)
res = sorted(t, key=lambda x: x.index)
print(res)
