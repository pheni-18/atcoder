# https://atcoder.jp/contests/abc106/tasks/abc106_b

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
    ans = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1

        if cnt == 8:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
