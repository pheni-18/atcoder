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

    n, q = inp()
    queries = [inp() for _ in range(q)]

    check_l = []

    for query in queries:
        p = query[0]
        if not p == 3:
            continue

        x = query[1]
        check_l.append(x)

    check_s = set(check_l)
    check_d = {}
    for c in check_l:
        check_d[c] = -1

    l = [[i] for i in range(n + 1)]
    for query in queries:
        x, y = None, None
        p = query[0]
        if p == 1:
            x, y = query[1:]

        elif p == 2:
            x, y = query[1:]
        else:
            x = query[1]
            p = check_d[x]
            if p == -1:
                print(1, x)
            else:
                pass




if __name__ == '__main__':
    main()
