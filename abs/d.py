data = [input() for _ in range(2)]

i = int(data[0])

l = data[1].split()
l = list(map(lambda x: int(x), l))

count = 0

end = False
while True:
    for i in l:
        if i % 2 == 1 or i == 0:
            end = True
            break
    else:
        count += 1
        l = list(map(lambda x: x / 2, l))
    if end:
        break
print(count)