lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']
z = zip(*[[int(i) for i in j.split()] for j in lst_in])
for i in z:
    print(*i)

