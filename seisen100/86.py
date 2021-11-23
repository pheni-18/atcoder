# https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja

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

    ans = 0
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if i == j:
                continue
        
            a, b = abl[j]
            uf.unite(a, b)

        cnt = 0
        for j in range(N):
            if uf.root(j) == j:
                cnt += 1

        if cnt > 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
