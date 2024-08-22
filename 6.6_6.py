lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']

d = {k: {i.split(':')[1].lstrip() for i in lst_in if i.split(':')[0] == k} for k in {i.split(':')[0] for i in lst_in}}
print(d)