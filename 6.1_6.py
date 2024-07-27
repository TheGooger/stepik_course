inp = 'лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина'
d = dict([i.split('=') for i in inp.split()])

if '3' in d:
    del d['3']
if 'False' in d:
    del d['False']
print(d)