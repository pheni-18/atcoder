data = [input() for _ in range(1)]

n, a, b = data[0].split()

n = int(n)
a = int(a)
b = int(b)

res = []

for i in range(1, n + 1):
    l = list(str(i))
    l = list(map(lambda x: int(x), l))
    if a <= sum(l) <= b:
        res.append(i)

print(sum(res))
