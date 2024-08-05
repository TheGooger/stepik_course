t = ('Воронеж', 'Самара', 'Тольятти', 'Ульяновск', 'Пермь')

if 'Ульяновск' in t:
    a = list(t)
    a.remove('Ульяновск')
    print(*tuple(a))
else:
    print(*t)