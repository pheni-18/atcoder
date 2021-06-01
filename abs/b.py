data = [input() for _ in range(1)]

i, j = data[0].split()
i = int(i)
j = int(j)

if i * j % 2 == 0:
    print("Even")
else:
    print("Odd")