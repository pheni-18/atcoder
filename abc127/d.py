def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    n, m = inp()
    al = inp()

    al = sorted(al)

    bcl = inps(m)
    bcl = sorted(bcl, key=lambda x: x[1], reverse=True)

    cur = 0
    for x in bcl:
        b, c = x
        for _ in range(b):
            if c > al[cur]:
                cur += 1
                al.append(c)
            else:
                break

    ansl = al[cur:]
    ans = sum(ansl)

    print(ans)

if __name__ == '__main__':
    main()
