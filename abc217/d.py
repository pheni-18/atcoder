def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import heapq
    from bisect import bisect_left

    l, q = inp()
    cxl = [inp() for _ in range(q)]

    memo = []
    for c, x in cxl:
        if c == 1:
            heapq.heappush(memo, x)
            print(memo)
        else:
            if len(memo) == 0:
                print(l)
                continue

            p = bisect_left(memo, x)
            if p == 0:
                print(memo[p])
            elif p == len(memo):
                print(l - memo[p - 1])
            else:
                print(memo[p] - memo[p - 1])


if __name__ == '__main__':
    main()
