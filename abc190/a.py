def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    a, b, c = inp()
    if a > b:
        print('Takahashi')
    elif b > a:
        print('Aoki')
    else:
        if c == 0:
            print('Aoki')
        else:
            print('Takahashi')


if __name__ == '__main__':
    main()
