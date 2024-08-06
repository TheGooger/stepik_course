lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']

name = tuple(tuple(i.split()) for i in lst_in)

print(name)