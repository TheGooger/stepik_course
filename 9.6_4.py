s = "10 5 4 -3 2 0 5 10 3"

lst = [int(i) for i in s.split()]

res = sorted(set(lst), reverse=True)[:4]

print(*res)