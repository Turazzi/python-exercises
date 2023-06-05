#odd and even lists

n = int(input())
numbers = input().split()
lista_n = []

i = 0
while i < len(numbers):
    n = int(numbers[i])
    lista_n.append(n)
    i += 1

i = 0
lista_a = []
lista_b = []
while i < len(lista_n):
    if lista_n[i] % 2 == 0:
        n = lista_n[i]
        lista_a.append(n)
    else:
        n = lista_n[i]
        lista_b.append(n)
    i += 1

i = 0
while i < len(lista_a):
    print(lista_a[i], end = ' ')
    i += 1
print()

i = 0
while i < len(lista_b):
    print(lista_b[i], end = ' ')
    i += 1
print()

