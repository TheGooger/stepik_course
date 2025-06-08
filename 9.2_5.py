def simple_num():
    k = 2
    while True:
        flag = True
        for i in range(1, k):
            if i != 1 and k % i == 0:
                flag = False
        if flag:
            yield k
        k += 1


numbers = simple_num()
for _ in range(20):
    print(next(numbers), end=" ")