# https://atcoder.jp/contests/abc120/tasks/abc120_d

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
    N, M = inp()
    abl = []
    for _ in range(M):
        a, b = inp()
        a -= 1
        b -= 1
        abl.append([a, b])

    ans = N * (N - 1) // 2
    ansl = [ans]
    uf = UnionFind(N)
    for i in range(M - 1):
        a, b = abl[-1 * (i + 1)]
        if not uf.is_same(a, b):
            ans -= uf.size(a) * uf.size(b)

        uf.unite(a, b)
        ansl.append(ans)

    ansl = reversed(ansl)
    for ans in ansl:
        print(ans)


if __name__ == '__main__':
    main()
