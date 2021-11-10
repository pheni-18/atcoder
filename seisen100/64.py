# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja

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
    V, E = inp()
    edges = []
    for _ in range(E):
        s, t, w = inp()
        d = {'s': s, 't': t, 'w': w}
        edges.append(d)

    edges = sorted(edges, key=lambda x: x['w'])

    ans = 0
    uf = UnionFind(V)
    for edge in edges:
        s = edge['s']
        t = edge['t']
        w = edge['w']

        if uf.is_same(s, t):
            continue

        ans += w
        uf.unite(s, t)

    print(ans)


if __name__ == '__main__':
    main()
