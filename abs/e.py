data = [input() for _ in range(4)]

am = int(data[0])
bm = int(data[1])
cm = int(data[2])
x = int(data[3])

cnt = 0

for i in range(am + 1):
    for j in range(bm + 1):
        for k in range(cm + 1):
            if i == 0 and j == 0 and k == 0:
                continue
            if x / (500 * i + 100 * j + 50 * k) == 1:
                cnt += 1

print(cnt)
