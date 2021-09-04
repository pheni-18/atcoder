def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import heapq

    q = inp()[0]
    queryl = [inp() for _ in range(q)]

    mode = 1
    s = []
    h = []
    cur = 0
    lenh = 0
    for query in queryl:
        if len(query) == 2:
            t, x = query
        else:
            t = query[0]

        if t == 1:
            s.append(x)
            heapq.heappush(h, x)
            mode = 1
        elif t == 2:
            if mode == 1:
                if lenh > 0:
                    v = heapq.heappop(h)
                    lenh -= 1
                    print(v)
                else:
                    v = s[cur]
                    print(v)
                    cur += 1
            elif mode == 3:
                v = heapq.heappop(h)
                print(v)
        elif t == 3:
            s = []
            cur = 0
            mode = 3
            lenh = len(h)


if __name__ == '__main__':
    main()
