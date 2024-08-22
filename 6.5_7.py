n = 210
d = (7, 5, 3, 2)
s = set()
for i in d:
    while n % i == 0:
        n /= i
        s.add(i)
print(s)
