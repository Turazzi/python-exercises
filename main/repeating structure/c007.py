#potentiation without '**'

a = int(input())
b = int(input())
i = 1
y = a

if b == 0:
    print(1)
elif b == 1:
    print(a)
elif a == 0:
    print(0)
else:
    while i < b:
        a = y * a
        i += 1

    print(a)