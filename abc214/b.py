def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    s, t = inp()
    cnt = 0
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if (i + j + k <= s) and (i * j * k <= t):
                    cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
