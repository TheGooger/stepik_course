def get_data_fig(*args, **kwargs):
    keys = ['tp', 'color', 'closed', 'width']
    res = (sum(args), )
    for i in keys:
        if i in kwargs.keys():
            res += (kwargs[i], )
    return res

print(get_data_fig(1, 2, 3, tp=True, color=7))
