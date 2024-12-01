lst_in = [1, 2, 3, 4]

def get_rec_sum(lst_in):
    if len(lst_in) == 1:
        return lst_in[0]
    a = lst_in.pop()
    return a + get_rec_sum(lst_in)


p = get_rec_sum(lst_in)
print(p)
