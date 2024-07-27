inp = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'

lst_in = inp.split()
#
# first = []
#
# for i in lst_in:
#     if i[:2] not in first:
#         first.append(i[:2])
# numbers = [[inp.split()[i] for i in range(len(inp.split())) if inp.split()[i][:2] == first[j]]
#            for j in range(len(first))]
#
# d = dict([[first[i], numbers[i]] for i in range(len(numbers))])
# print(d)

d = dict([(j[:2], [i for i in lst_in if j[:2] == i[:2]]) for j in lst_in])
#d = dict([(x[:2], [i for i in lst_in if x[:2] == i[:2]]) for x in lst_in])

print(d)