lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']

# d = {}
#
# for i in range(len(lst_in)):
#     if lst_in[i].split()[1] not in d:
#         d[lst_in[i].split()[1]] = [lst_in[i].split()[0]]
#     else:
#         d[lst_in[i].split()[1]].append(lst_in[i].split()[0])
#
# print(d)


lst = [i.split() for i in lst_in]
# d = dict([(x[1], [i[0] for i in lst if x[1] == i[1]]) for x in lst])

d = dict([(x[1], [i[0] for i in lst if x[1] == i[1]]) for x in lst])
# names = []
# for i in lst_in:
#     if i.split()[1] not in names:
#         names.append(i.split()[1])
# # lst = [[(names[i], [lst_in[j].split()[0]]) for j in range(len(lst_in)) if lst_in[j].split()[1] == names[i]]
# #        for i in range(len(names))]
#
# lst = [[lst_in[i].split()[1], lst_in[i].split()[0]] for i in range(len(lst_in))]
#
# print(lst)