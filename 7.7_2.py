N = 8

def get_rec_N(N):
    if N > 1:
        get_rec_N(N-1)
    print(N)

get_rec_N(N)