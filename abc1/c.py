# n = int(input())
row = 1
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

def il2sl(l):
    return list(map(lambda x: str(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""

from decimal import Decimal, ROUND_HALF_UP

def create_dir(deg):
    if 112.5 <= deg < 337.5:
        return 'NNE'
    elif 337.5 <= deg < 562.5:
        return 'NE'
    elif 562.5 <= deg < 787.5:
        return 'ENE'
    elif 787.5 <= deg < 1012.5:
        return 'E'
    elif 1012.5 <= deg < 1237.5:
        return 'ESE'
    elif 1237.5 <= deg < 1462.5:
        return 'SE'
    elif 1462.5 <= deg < 1687.5:
        return 'SSE'
    elif 1687.5 <= deg < 1912.5:
        return 'S'
    elif 1912.5 <= deg < 2137.5:
        return 'SSW'
    elif 2137.5 <= deg < 2362.5:
        return 'SW'
    elif 2362.5 <= deg < 2587.5:
        return 'WSW'
    elif 2587.5 <= deg < 2812.5:
        return 'W'
    elif 2812.5 <= deg < 3037.5:
        return 'WNW'
    elif 3037.5 <= deg < 3262.5:
        return 'NW'
    elif 3262.5 <= deg < 3487.5:
        return 'NNW'
    else:
        return 'N'

def create_w(dis):
    d = Decimal(str(dis / 60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    d = float(d)

    if 0 <= d <= 0.2:
        return 0
    elif d <= 1.5:
        return 1
    elif d <= 3.3:
        return 2
    elif d <= 5.4:
        return 3
    elif d <= 7.9:
        return 4
    elif d <= 10.7:
        return 5
    elif d <= 13.8:
        return 6
    elif d <= 17.1:
        return 7
    elif d <= 20.7:
        return 8
    elif d <= 24.4:
        return 9
    elif d <= 28.4:
        return 10
    elif d <= 32.6:
        return 11
    else:
        return 12

deg, dis = sl2il(inp[0].split())
dir_ = create_dir(deg)
w = create_w(dis)
if w == 0:
    dir_ = 'C'

print(dir_, w)


