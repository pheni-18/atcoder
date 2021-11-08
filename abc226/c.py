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
    from collections import deque

    N = inp_one()
    tl = []
    kl = []
    all = []
    for _ in range(N):
        x = inp()
        t = x[0]
        k = x[1]
        tl.append(t)
        kl.append(k)

        if len(x) > 2:
            al = x[2:]
        else:
            al = []
        all.append(al)

    to = [[] for _ in range(N)]
    for i in range(N):
        al = all[i]
        for a in al:
            a -= 1
            to[i].append(a)

    ans = 0
    visited = [False] * N
    dq = deque()
    dq.append(N - 1)
    while dq:
        u = dq.popleft()
        if visited[u]:
            continue

        for v in to[u]:
            dq.append(v)

        ans += tl[u]
        visited[u] = True

    print(ans)


if __name__ == '__main__':
    main()
