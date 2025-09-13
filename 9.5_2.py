lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']




a = zip(*zip(*map(lambda s: s.replace(" ", ""), lst_in)))
list(map(print, a))
# for i in a:
#     print(i)

# list(map(print, *zip(*map(str.split, lst_in))))