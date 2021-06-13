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
    a, b, c = inp()

    if c % 2 == 0:
        if abs(a) == abs(b):
            print('=')
            return
        elif abs(a) > abs(b):
            print('>')
            return
        else:
            print('<')
            return
    else:
        if a >= 0 and b >= 0:
            if abs(a) == abs(b):
                print('=')
                return
            elif abs(a) > abs(b):
                print('>')
                return
            else:
                print('<')
                return
        elif a < 0 and b < 0:
            if abs(a) == abs(b):
                print('=')
                return
            elif abs(a) > abs(b):
                print('<')
                return
            else:
                print('>')
                return
        elif a < 0:
            print('<')
            return
        else:
            print('>')
            return


if __name__ == '__main__':
    main()
