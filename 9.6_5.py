s_1 = "7 6 4 2 6 7 9 10 4"
s_2 = "-4 5 10 4 5 65"

lst_1 = list(map(int, s_1.split()))
lst_2 = list(map(int, s_2.split()))

lst_1.sort()
lst_2.sort(reverse=True)

print(*list(map(sum, zip(lst_1, lst_2))))