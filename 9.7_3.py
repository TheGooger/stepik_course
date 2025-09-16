lst_in = list("до фа соль до ре фа ля си".split())

d = {'до': 0, 'ре': 1, 'ми': 2, 'фа': 3, 'соль': 4, 'ля': 5, 'си': 6}
res = sorted(lst_in, key=lambda x: d[x])


print(res)