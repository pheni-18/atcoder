# https://atcoder.jp/contests/abc065/tasks/arc076_b

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
    N = inp_one()
    xyl = []
    for i in range(N):
        x, y = inp()
        d = {'i': i, 'x': x, 'y': y}
        xyl.append(d)

    xyl_sorted_x = sorted(xyl, key=lambda d: d['x'])
    xyl_sorted_y = sorted(xyl, key=lambda d: d['y'])

    edges = []
    for i in range(1, N):
        d1 = xyl_sorted_x[i - 1]
        d2 = xyl_sorted_x[i]
        cost = abs(d1['x'] - d2['x'])
        d = {'u': d1['i'], 'v': d2['i'], 'cost': cost}
        edges.append(d)

        d1 = xyl_sorted_y[i - 1]
        d2 = xyl_sorted_y[i]
        cost = abs(d1['y'] - d2['y'])
        d = {'u': d1['i'], 'v': d2['i'], 'cost': cost}
        edges.append(d)

    edges = sorted(edges, key=lambda d: d['cost'])

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

    print(ans)


if __name__ == '__main__':
    main()
