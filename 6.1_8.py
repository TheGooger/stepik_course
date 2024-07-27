lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']

names = []
for i in lst_in:
    if i.split()[1] not in names:
        names.append(i.split()[1])
lst = [[(names[i], [lst_in[j].split()[0]]) for j in range(len(lst_in)) if lst_in[j].split()[1] == names[i]]
       for i in range(len(names))]
print(lst)