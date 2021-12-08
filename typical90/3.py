# ☆4

# 木の直径、DFS


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
    import sys
    sys.setrecursionlimit(10 ** 5 + 1)

    N = inp_one()
    to = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = inp()
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)
    
    dists = [-1] * N
    d = 0
    def dfs(u, f):
        nonlocal d

        for v in to[u]:
            if v == f:
                continue

            if dists[v] != -1:
                continue
            
            d += 1
            dfs(v, u)
            d -= 1

        dists[u] = d

    dists[0] = 0
    dfs(0, -1)
    max_d = max(dists)
    p1 = dists.index(max_d)

    dists = [-1] * N
    dists[p1] = 0
    dfs(p1, -1)
    max_d = max(dists)
    print(max_d + 1)
    

if __name__ == '__main__':
    main()
