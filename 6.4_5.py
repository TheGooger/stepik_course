# l = ['Python', '3.9.11', '-', 'best', 'language!']
# dig = list(map(str, range(10)))
# s = set()
# for i in dig:
#     for j in l:
#         if i in j:
#             s.add(i)
# if s:
#     print(*sorted(s))
# else:
#     print('НЕТ')

inp = 'Python 3.9.11 - best language!'
# s = set([i for i in input() if i.isdigit()])
# if s:
#     print(*sorted(s))
# else:
#     print('НЕТ')
print(*sorted(set([i for i in inp if i.isdigit()])) if set([i for i in inp if i.isdigit()]) else ['НЕТ'])
