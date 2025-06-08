a = 0
b = 10

gen = (0.5 * pow(x, 2) - 2.0 for x in (a + 0.01 * y for y in range(0, 100*(b-a) + 1)))

for _ in range(20):
    print(round(next(gen), 2))

