menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
lst_in = ['a=url_1', 'b=url_2']
dict_in = {}
for i in range(len(lst_in)):
    dict_in[lst_in[i].split('=')[0]] = lst_in[i].split('=')[1]
menu = {**menu, **dict_in} 
print(menu)