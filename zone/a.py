def inp(to_int=False):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    l = sl2il(l) if to_int else l
    return l[0] if len(l) == 1 else l


def inps(n, to_int=False):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def sl2il(l):
    return list(map(lambda x: int(x), l))


def il2sl(l):
    return list(map(lambda x: str(x), l))


def main():
    s = inp()
    sl = list(s)
    ans = 0
    for i in range(9):
        if sl[i] == 'Z' and sl[i+1] == 'O' and sl[i+2] == 'N' and sl[i+3] == 'e':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
