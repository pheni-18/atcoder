def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    s1, s2, s3, s4 = [inp(False)[0] for _ in range(4)]
    s = {s1, s2, s3, s4}
    if len(s) == 4:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
