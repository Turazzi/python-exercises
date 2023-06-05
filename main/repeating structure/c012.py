#greater number

n = int(input())
m = int(input())
maior = m
i = 1

while i < n:
    m = int(input())
    i += 1
    if m > maior:
        maior = m

print(maior)