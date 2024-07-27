n = int(input())
d = {}

while n != 0:
    if n not in d:
        sq = n ** 0.5
        d[n] = sq
        print(f'{sq:.3}')
    else:
        print(f'значение из кэша: {d[n]:.3}')
    n = int(input())