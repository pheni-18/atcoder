def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]
    al = inp()
    al2 = []
    for i in range(len(al)):
        al2.append({'k': i + 1, 'v': al[i]})

    al2 = sorted(al2, key=lambda x: x['v'])
    print(al2[-2]['k'])


if __name__ == '__main__':
    main()
