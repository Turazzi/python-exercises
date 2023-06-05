#typed sequence sum

x = 1
i = 0
j = 0
k = 0

while x != 0:
    x = int(input())
    if (x % 2) == 0:
        i += x
    else:
        j += x
    k += x
    
print(i)
print(j)
print(k)