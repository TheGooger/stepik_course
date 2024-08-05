names = ('Петя', 'Варвара', 'Венера', 'Василиса', 'Василий', 'Федор')
# for i in names:
#     if 'ва' in i.lower():
#         print(i.lower(), end=' ')

print(*[a.lower() for a in names if 'ва' in a.lower()])