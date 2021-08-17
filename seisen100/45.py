# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp

# DP

# TODO: fix TLE

def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    nl = []
    ml = []
    cll = []
    xll = []

    # f = open('/Users/mitsuyoshi/Downloads/45in.txt', 'r')
    #
    # def inp(to_int=True):
    #     if not type(to_int) == bool:
    #         raise Exception()
    #     nonlocal f
    #     l = f.readline()
    #     l = l.rstrip('\n')
    #     l = l.split()
    #     return list(map(lambda x: int(x), l)) if to_int else l

    while True:
        n, m = inp()
        if n == 0 and m == 0:
            break

        nl.append(n)
        ml.append(m)
        cll.append([inp()[0] for _ in range(m)])
        xll.append([inp()[0] for _ in range(n)])
    # f.close()

    for i in range(len(nl)):
        n, m, cl, xl = nl[i], ml[i], cll[i], xll[i]

        dp = [[(510 ** 2) * 20000 + 1] * 256 for _ in range(n + 1)]
        dp[0][128] = 0

        for j in range(n):
            x = xl[j]
            for y in range(256):
                for l in range(m):
                    c = cl[l]
                    y2 = y + c
                    if y2 > 255:
                        y2 = 255
                    elif y2 < 0:
                        y2 = 0

                    v = (y2 - x) ** 2
                    dp[j + 1][y2] = min(dp[j + 1][y2], dp[j][y] + v)

        print(min(dp[-1]))


if __name__ == '__main__':
    main()
