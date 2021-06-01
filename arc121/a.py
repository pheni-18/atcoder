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
    n = inp()[0]
    xs = []
    ys = []

    for i in range(n):
        x, y = inp()
        xs.append({'k': i, 'v': x})
        ys.append({'k': i, 'v': y})

    xs = sorted(xs, key=lambda z: z['v'], reverse=True)
    ys = sorted(ys, key=lambda z: z['v'], reverse=True)

    l = []
    l.append({'k': {xs[0]['k'], xs[-1]['k']}, 'v': abs(xs[0]['v'] - xs[-1]['v'])})
    l.append({'k': {xs[0]['k'], xs[-2]['k']}, 'v': abs(xs[0]['v'] - xs[-2]['v'])})
    l.append({'k': {xs[1]['k'], xs[-1]['k']}, 'v': abs(xs[1]['v'] - xs[-1]['v'])})
    l.append({'k': {ys[0]['k'], ys[-1]['k']}, 'v': abs(ys[0]['v'] - ys[-1]['v'])})
    l.append({'k': {ys[0]['k'], ys[-2]['k']}, 'v': abs(ys[0]['v'] - ys[-2]['v'])})
    l.append({'k': {ys[1]['k'], ys[-1]['k']}, 'v': abs(ys[1]['v'] - ys[-1]['v'])})

    l = sorted(l, key=lambda z: z['v'])
    if l[-1]['k'] == l[-2]['k']:
        print(l[-3]['v'])
    else:
        print(l[-2]['v'])


if __name__ == '__main__':
    main()
