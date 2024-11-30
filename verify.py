import sys

# здесь объявляйте функцию
def is_isolate(x, y, lst2D):
    min_i = max(0, y - 1)
    max_i = min(len(lst2D) - 1, y + 1)
    min_j = max(0, x - 1)
    max_j = min(len(lst2D) - 1, x + 1)
    sum = 0
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            sum += lst2D[i][j]
    return True if sum == 1 else False


def verify(lst2D):
    for i in range(len(lst2D)):
        for j in range(len(lst2D)):
            if lst2D[i][j] == 1:
                if not is_isolate(j, i, lst2D):
                    return False
    return True

lines = ['1 0 0 0 0\n', '0 0 1 0 0\n', '0 0 0 0 0\n', '0 1 0 1 0\n', '0 0 0 0 0']

lst2D = [[int(i) for i in lines[j].replace(" ", "").replace('\n', '')] for j in range(len(lines))]
print(verify(lst2D))