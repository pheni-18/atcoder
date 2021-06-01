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
    from collections import deque
    s = inp()
    d = deque()
    re = False
    for c in s:
        if c == 'R':
            re = not re
            continue

        if re:
            d.appendleft(c)
        else:
            d.append(c)

    if re:
        d = list(reversed(d))
    ansl = []
    for c in d:
        if len(ansl) > 0:
            if ansl[-1] == c:
                ansl.pop()
                continue
        ansl.append(c)

    ans = ''.join(ansl)

    print(ans)


if __name__ == '__main__':
    main()
