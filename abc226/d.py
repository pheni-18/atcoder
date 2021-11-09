def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inp_one(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    s = input()
    return int(s) if to_int else s


def main():
    import math

    N = inp_one()
    xyl = [inp() for _ in range(N)]

    se = set()
    for i in range(N):
        x1, y1 = xyl[i]
        for j in range(N):
            if i == j:
                continue

            x2, y2 = xyl[j]
            dx, dy = x1 - x2, y1 - y2
            g = math.gcd(dx, dy)
            t = (dx // g, dy // g)
            se.add(t)

    ans = len(se)
    print(ans)


if __name__ == '__main__':
    main()
