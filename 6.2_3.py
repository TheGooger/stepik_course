inp = 'Сергей Балакирев'
d = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': "--.", 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..',
    'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...',
    'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--',
    'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'
}
res = []
for i in input().lower().replace('ё', 'е'):
    res.append(d.get(i))
print(' '.join(res))
