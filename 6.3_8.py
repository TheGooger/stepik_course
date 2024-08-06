t = (3, 4, 2, -1, -1, 3, 2, 10, 11, 3, 4)
# k = 0
# for i in  t:
#     if t.count(i) > 1:
#         print(t.index(i, k), end=' ')
#     k += 1

print(*[i for i, v in enumerate(t) if t.count(v) > 1])