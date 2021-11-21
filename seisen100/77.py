# https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a

# 累積和


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
    n, m = inp()
    sl = [0]
    for _ in range(n - 1):
        sl.append(inp_one())
    al = [inp_one() for _ in range(m)]

    total = [0]
    for i in range(n):
        v = total[i] + sl[i]
        total.append(v)

    ans = 0
    prev = 1
    for a in al:
        ans += abs(total[prev + a] - total[prev])
        ans %= 10 ** 5
        prev += a

    print(ans)


if __name__ == '__main__':
    main()
