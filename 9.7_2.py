lst_in = [
          'ножницы=100',
          'котелок=500',
          'спички=20',
          'зажигалка=40',
          'зеркальце=50'
         ]

d = {i.split('=')[0]: int(i.split('=')[1]) for i in lst_in}
lst = sorted(d.keys(), key=lambda x: d[x], reverse=True)
print(lst)