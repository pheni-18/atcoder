# https://atcoder.jp/contests/sumitrust2019/submissions/me

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
    s = inp(False)[0]

    ans = 0
    for i in range(1000):
        ca = str(i).zfill(3)
        cur = 0
        for j in range(n):
            if s[j] == ca[cur]:
                cur += 1
            if cur == 3:
                ans += 1
                break

    print(ans)


if __name__ == '__main__':
    main()
