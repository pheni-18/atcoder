def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    x, y = inp()
    abl = [inp() for _ in range(n)]




if __name__ == '__main__':
    main()
