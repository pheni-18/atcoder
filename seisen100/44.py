# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp

# DP

def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    nl = []
    while True:
        n = inp()[0]
        if n == 0:
            break
        nl.append(n)

    m = 10 ** 6
    dp = [m] * (m + 1)
    dp[0] = 0
    dp_odd = [m] * (m + 1)
    dp_odd[0] = 0
    for i in range(1, 10 ** 3):
        s = i * (i + 1) * (i + 2) // 6
        if s > m:
            break

        for j in range(m - s):
            v = dp[j] + 1
            if v < dp[j + s]:
                dp[j + s] = v

        if s & 1:
            for j in range(m - s):
                v = dp_odd[j] + 1
                if v < dp_odd[j + s]:
                    dp_odd[j + s] = v

    for n in nl:
        print(dp[n], dp_odd[n])


if __name__ == '__main__':
    main()
