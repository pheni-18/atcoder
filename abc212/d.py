def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import heapq

    n = inp()[0]
    ql = [inp() for _ in range(n)]

    h = []
    s = 0
    for q in ql:
        p = q[0]
        x = None
        if p == 1 or p == 2:
            x = q[1]

        if p == 1:
            heapq.heappush(h, x - s)
        elif p == 2:
            s += x
        else:
            v = heapq.heappop(h)
            print(v + s)


if __name__ == '__main__':
    main()
