things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
th = {value: key for key, value in things.items()}

n = 1000 * 10
w = sorted(th.keys(), reverse=True)
res = []
for i in w:
    if n - i >= 0:
        n -= i
        res.append(th[i])
    elif n == 0:
        break
#
# while n >= 0:
#     if n - w[i] >= 0:
#         n -= w[i]
#         res.append(th[w[i]])
#         i += 1
#     else:
#         i += 1
#         continue
print(*res)

# print(sorted(things.values(), reverse=True))

