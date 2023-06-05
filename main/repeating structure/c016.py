#sum of prime numbers

n = int(input())
i = 2
soma = 0

while i <= n:
    j = 2
    prime = True
    while j < i:
        if i % j == 0:
            prime = False
            j += 1
            break
        j += 1
    if prime:
        soma += i
    i += 1
print(soma)
