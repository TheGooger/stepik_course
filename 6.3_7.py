t = (8, 11, -5, -2, 8, 11, -5)
n_t = tuple()

for i in t:
    if i not in n_t:
        n_t += i,

print(*n_t)
