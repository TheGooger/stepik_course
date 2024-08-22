inp = ['и', 'что', 'сказать', 'и', 'что', 'сказать', 'и', 'нечего', 'и', 'точка']
s_k = {i for i in inp}
d = {key: inp.count(key) for key in s_k}
print(d.get('и', 0))