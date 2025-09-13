s = "-2 -1 8 11 4 5"

lst = list(map(int, s.split()))
lst.sort()

tp_lst = tuple(sorted(map(int, s.split())))

print(lst)
print(tp_lst)