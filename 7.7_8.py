lst_in = [8, 11, -6, 3, 0, 1, 1]

def sort(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] >= b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    c = c + a[i:] + b[j:]
    return c 

def divide_in_two(lst_in):
    N = len(lst_in) // 2
    a_1 = lst_in[:N]
    a_2 = lst_in[N:]
    if len(a_1) > 1:
        a_1 = divide_in_two(a_1)
    if len(a_2) > 1:
        a_2 = divide_in_two(a_2)
    return sort(a_1, a_2)
      

print(divide_in_two(lst_in))