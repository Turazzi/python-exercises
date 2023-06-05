#birthday candles

age = int(input())
h = 0
i = 0
largest = 0
i2 = 0
aux = 0

while i < age:
    h = int(input())
    i += 1
    if h > largest:
        largest = h
        i2 = 1
    elif h == largest:
        i2 += 1

print(i2)