# 双方向リスト


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
    n, q = inp()
    queries = [inp() for _ in range(q)]

    front = [-1] * n
    back = [-1] * n

    for query in queries:
        type = query[0]
        if type == 3:
            x = query[1]
            x -= 1
            while front[x] != -1:
                x = front[x]
            ansl = [str(x + 1)]
            while back[x] != -1:
                x = back[x]
                ansl.append(str(x + 1))

            print(str(len(ansl)) + ' ' + ' '.join(ansl))
        else:
            x, y = query[1:]
            x -= 1
            y -= 1

            if type == 1:
                back[x] = y
                front[y] = x
            else:
                back[x] = -1
                front[y] = -1


if __name__ == '__main__':
    main()
