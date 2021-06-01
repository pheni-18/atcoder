data = [input() for _ in range(2)]
n = int(data[0])
l = data[1].split()
end = False
ans = 0
max = 0
jmax = 0
for j in l:
    if int(j) > jmax:
        jmax = int(j)


for j in range(2, jmax + 1):
    cnt = 0
    for i in l:
        if int(i) % j == 0:
            cnt += 1
            if cnt == n:
                ans = j
                end = True
                break
            if cnt > max:
                max = cnt
                ans = j
    if end:
        break
print(ans)
