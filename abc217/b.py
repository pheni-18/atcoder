def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    s1 = inp(False)[0]
    s2 = inp(False)[0]
    s3 = inp(False)[0]

    l = ['ABC', 'ARC', 'AGC', 'AHC']
    l.remove(s1)
    l.remove(s2)
    l.remove(s3)
    print(l[0])


if __name__ == '__main__':
    main()
