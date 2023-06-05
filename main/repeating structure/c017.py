#sum of the factorials

n = int(input())

soma = 0
i = 0


while i <= n:
    j = 1
    fat = 1
    while j <= i:
        fat *= j
        j += 1
    soma += fat
    i += 1

print(soma)
