t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

N = 3
# t2 = ()
# temp = ()
#
# for i in range(N):
#     for j in range(N):
#         temp += t[i][j],
#     t2 += (temp),
#     temp = ()
t2 = tuple(t[i][:N] for i in range(N))
for i in t2:
    print(*i)
print(t2)