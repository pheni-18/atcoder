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
    kukans = []
    for _ in range(n):
        kukans.append(inp())

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            k1 = kukans[i]
            k2 = kukans[j]

            if k1[2] >= k2[2]:
                rk = k1
                lk = k2
            else:
                rk = k2
                lk = k1

            if rk[1] > lk[2]:
                continue
            elif rk[1] == lk[2]:
                if not (rk[0] in [1, 2] and lk[0] in [1, 3]):
                    continue

            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
