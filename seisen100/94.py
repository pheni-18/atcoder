# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1149&lang=jp

# 実装問題


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
    nwdl = []
    psll = []
    while True:
        n, w, d = inp()
        if n == 0 and w == 0 and d == 0:
            break
        nwdl.append([n, w, d])

        psl = [inp() for _ in range(n)]
        psll.append(psl)

    for nwd, psl in zip(nwdl, psll):
        n, w, d = nwd
        cakes = [[w, d]]
        for p, s in psl:
            p -= 1
            x, y = cakes.pop(p)
            s %= x * 2 + y * 2
            if 0 < s < x:
                q = s
                piece1 = [q, y]
                piece2 = [(x - q), y]
            elif s < x + y:
                q = s - x
                piece1 = [x, q]
                piece2 = [x, (y - q)]
            elif s < x * 2 + y:
                q = s - x - y
                piece1 = [q, y]
                piece2 = [(x - q), y]
            else:
                q = s - x - y - x
                piece1 = [x, q]
                piece2 = [x, (y - q)]

            if piece1[0] * piece1[1] > piece2[0] * piece2[1]:
                cakes.append(piece2)
                cakes.append(piece1)
            else:
                cakes.append(piece1)
                cakes.append(piece2)

        ansl = [l[0] * l[1] for l in cakes]
        ansl = sorted(ansl)
        ansl = [str(ans) for ans in ansl]
        print(' '.join(ansl))


if __name__ == '__main__':
    main()
