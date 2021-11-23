# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja

# Union-Find


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
    n, q = inp()
    queries = [inp() for _ in range(q)]

    uf = UnionFind(n)
    for query in queries:
        com, x, y = query
        if com == 0:
            uf.unite(x, y)
        elif com == 1:
            if uf.is_same(x, y):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()
