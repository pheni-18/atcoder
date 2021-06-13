# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

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
    n = inp()[0]

    abl = []
    stl = []
    for i in range(n):
        a, b = inp()
        abl.append([a, b])
        stl.append(a)
        stl.append(b)

    stl = sorted(stl)

    ans = float('inf')
    for i in range(2 * n):
        for j in range(i, 2 * n):
            s = stl[i]
            t = stl[j]
            sec = 0
            for k in range(n):
                a = abl[k][0]
                b = abl[k][1]
                sec += abs(a - b) + abs(s - a) + abs(t - b)

            ans = min(ans, sec)

    print(ans)


if __name__ == '__main__':
    main()
