# n = int(input())

def sl2il(l):
    return list(map(lambda x: int(x), l))

def il2sl(l):
    return list(map(lambda x: str(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""


def main():
    row = 3
    inp = [input() for _ in range(row)]

    n = int(inp[0])
    s = inp[1]
    q = int(inp[2])

    sl = [[], []]
    sl[0] = list(s[:n])
    sl[1] = list(s[n:])

    for _ in [0] * q:
        inp = input()
        query = sl2il(inp.split())
        if query[0] == 1:
            ai = query[1] - 1
            bi = query[2] - 1
            sl[ai//n][ai%n], sl[bi//n][bi%n] = sl[bi//n][bi%n], sl[ai//n][ai%n]
        else:
            sl[0], sl[1] = sl[1], sl[0]

    l = []
    l.extend(sl[0])
    l.extend(sl[1])
    print(''.join(l))


main()
