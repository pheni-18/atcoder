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


class UnionFind:
    def __init__(self, n: int):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]

        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]


def main():
    N, M = inp()
    abl = []
    for _ in range(M):
        a, b = inp()
        abl.append([a - 1, b - 1])

    if M == 0:
        print('Yes')
        return

    uf = UnionFind(N)
    abl = sorted(abl, key=lambda x: (x[0], x[1]))
    lrl = [[i, i] for i in range(N)]
    for i in range(M):
        a, b = abl[i]
        if uf.is_same(a, b):
            print('No')
            return

        c = uf.root(a)
        d = uf.root(b)
        l1, r1 = lrl[c]
        l2, r2 = lrl[d]
        if a not in [l1, r1]:
            print('No')
            return
        if b not in [l2, r2]:
            print('No')
            return

        uf.unite(a, b)
        e = uf.root(a)
        if a == l1:
            lrl[e][1] = r1
            if b == l2:
                lrl[e][0] = r2    
            else:
                lrl[e][0] = l2
        else:
            lrl[e][0] = l1
            if b == l2:
                lrl[e][1] = r2
            else:
                lrl[e][1] = l2

    print('Yes')


if __name__ == '__main__':
    main()
