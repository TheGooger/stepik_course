lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
          'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii',
          'ustanovka-i-poryadok-raboty-pycharm']
d = {}
for i in lst_in:
    if i not in d:
        d[i] = f'HTML-страница для адреса {i}'
        print(d[i])
    else:
        print(f'Взято из кэша: {d[i]}')