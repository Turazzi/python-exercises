#sorted values

n = int(input())
m = int(input())
maior = 0
menor = m

i = 1
i2 = 1
i3 = 1
while i < n:
    m = int(input())
    if m >= maior:
        maior = m
        i2 += 1
    if m <= menor:
        menor = m
        i3 += 1
    i += 1
if i2 == i:
    print(1)
if i3 == i:
    print(-1)
if i2 != i and i3 != i:
    print(0)
