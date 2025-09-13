inp = "Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь"

lst_in = iter(inp.split())

res = zip(lst_in, lst_in, lst_in)

for i in res:
    print(*i)