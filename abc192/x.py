
def f1(x, n):
    out = 0
    for i in range(1, len(str(x)) + 1):
        out += int(x[-i]) * (n**(i - 1))
    return out