def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    s = inp(False)[0]
    sl = list(s)

    for i in range(n):
        if sl[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')

            break


if __name__ == '__main__':
    main()
