# TODO: Challenge

def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    from queue import Queue
    n = inp()[0]
    to = [[]] * n
    cost = [[]] * n
    for i in range(n - 1):
        u, v, w = inp()
        u -= 1
        v -= 1
        to[u].append(v)
        cost[u].append(w)
        to[v].append(u)
        cost[v].append(u)

    ansl = [-1] * n
    q = Queue()

    ansl[0] = 0
    q.put(0)

    while not q.empty():
        a = q.get()
        for i in range(len(to[a])):
            b = to[a][i]
            w = cost[a][i]
            if ansl[b] != -1:
                continue
            ansl[b] = (ansl[a] + w) % 2
            q.put(b)

    for ans in ansl:
        print(ans)


if __name__ == '__main__':
    main()
