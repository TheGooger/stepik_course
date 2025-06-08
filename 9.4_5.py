import re


email_list = ["тест_почта@mail.ru", "test_post@mail.ru", "test_post@мэил.ру"]

regEmail = re.compile(r'^\w+@\w+\.\w+$', re.A) # теперь в \w кириллица, чтобы избежать
                                                      # нужен флаг A (ACSII

for i in email_list:
    temp = regEmail.search(i)
    if temp:
        print(temp.group())
    else:
        print(temp)


""" Решение с сайта:
import re


email_list = input().split()

regEmail = re.compile(r'^\w+@\w+\.\w+$', re.A)

print(*filter(lambda i: regEmail.search(i) != None, email_list))"""