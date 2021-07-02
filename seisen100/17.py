# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja

# 順列全探索


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
    from itertools import permutations

    k = inp()[0]
    B_LEN = 8
    queens = [-1] * B_LEN
    for _ in range(k):
        r, c = inp()
        queens[r] = c

    ansl = []
    l = [i for i in range(B_LEN)]
    for t in permutations(l):
        flg = False
        for i in range(B_LEN):
            if queens[i] == -1:
                continue

            if not queens[i] == t[i]:
                flg = True

        if flg:
            continue

        ok = True
        for r, c in enumerate(t):
            for i in range(1, B_LEN):
                for pm in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                    x = r + (i * pm[0])
                    y = c + (i * pm[1])
                    if not (0 <= x <= B_LEN - 1 and 0 <= y <= B_LEN - 1):
                        continue

                    if t[x] == y:
                        ok = False
                        break

                if not ok:
                    break

        if ok:
            ansl = list(t)

    for i in ansl:
        l = ['.'] * B_LEN
        l[i] = 'Q'
        print(''.join(l))


if __name__ == '__main__':
    main()
