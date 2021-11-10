# https://www.ioi-jp.org/camp/2010/2010-sp-tasks/2010-sp-day3_22.pdf

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
    N, M, K = inp()
    edges = []
    for _ in range(M):
        a, b, c = inp()
        a -= 1
        b -= 1
        d = {'a': a, 'b': b, 'c': c}
        edges.append(d)

    edges = sorted(edges, key=lambda x: x['c'])

    costs = []
    uf = UnionFind(N)
    for edge in edges:
        a = edge['a']
        b = edge['b']
        c = edge['c']

        if uf.is_same(a, b):
            continue

        costs.append(c)
        uf.unite(a, b)

    saving = 0
    for i in range(K - 1):
        cur = N - 2 - i
        saving += costs[cur]

    ans = sum(costs) - saving
    print(ans)


if __name__ == '__main__':
    main()
