ns = input()
ans = -1

l = list(ns)
amari = int(ns) % 3
if amari == 0:
    ans = 0
elif amari == 1:
    cnt = 0
    for j in l:
        if amari == int(j) % 3:
            ans = 1
            break
        elif int(j) % 3 == 2:
            cnt += 1
    else:
        if cnt >= 2:
            ans = 2
elif amari == 2:
    cnt = 0
    for j in l:
        if amari == int(j) % 3:
            ans = 1
            break
        elif int(j) % 3 == 1:
            cnt += 1
    else:
        if cnt >= 2 and :
            ans = 2
print(ans)