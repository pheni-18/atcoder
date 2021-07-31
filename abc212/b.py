def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    p = inp(False)[0]
    pl = list(p)
    pl = [int(v) for v in pl]
    if pl[0] == pl[1] == pl[2] == pl[3]:
        print('Weak')
        return

    cnt = 0
    for i in range(3):
        if ((pl[i] + 1) % 10) == pl[i + 1]:
            cnt += 1

    if cnt == 3:
        print('Weak')
        return

    print('Strong')


if __name__ == '__main__':
    main()
