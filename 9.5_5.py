s = "Sergey Balakirev"

# res = ((letter, index) for index, letter in enumerate(s))
# lst = [i for i in res if i[1] < 10]

lst = list(zip(s, range(len(s))))[:10]

print(lst)