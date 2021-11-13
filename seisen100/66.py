# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127

# 最小全域木問題


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
    import math

    NL = []
    cells_l = []
    while True:
        N = inp_one()
        if N == 0:
            break

        NL.append(N)

        cells = []
        for _ in range(N):
            cell = inp(False)
            cell = list(map(lambda x: float(x), cell))
            cells.append(cell)

        cells_l.append(cells)

    for ii in range(len(NL)):
        N = NL[ii]
        cells = cells_l[ii]

        edges = []
        for i in range(N):
            x1, y1, z1, r1 = cells[i]
            for j in range(i + 1, N):
                x2, y2, z2, r2 = cells[j]
                d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
                cost = d - r1 - r2
                cost = cost if cost > 0 else 0
                e = {'u': i, 'v': j, 'cost': cost}
                edges.append(e)

        edges = sorted(edges, key=lambda x: x['cost'])

        ans = 0
        uf = UnionFind(N)
        for edge in edges:
            u = edge['u']
            v = edge['v']
            cost = edge['cost']

            if uf.is_same(u, v):
                continue

            ans += cost
            uf.unite(u, v)

        print(f'{ans:.3f}')


if __name__ == '__main__':
    main()
