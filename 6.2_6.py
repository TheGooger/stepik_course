lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
d = {}
# d = dict.fromkeys([i.split()[0] for i in lst_in], [])
# for i in d:
#     d[i] = []
#     for j in lst_in:
#         if j.split()[0] == i:
#             d[i].append(j.split()[1])



for i in lst_in:
    k, v = i.split()
    d[k] = d.get(k, []) + [v]

for k, v in d.items():
    print(f'{int(k)}:', ', '.join(v))
