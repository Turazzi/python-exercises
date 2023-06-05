#major, minor and sum

n = int(input())
m = int(input())
maior = m
menor = m
soma = 0
i = 1
soma += m
while i < n:
    m = int(input())
    i += 1
    if m > maior:
        maior = m
    elif m < menor:
        menor = m
        soma  +=  m

print(maior)
print(menor)
print(soma)