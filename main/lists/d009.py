#sum of segments

n = int(input())
numbers = input().split()
lista_a = []
positions = input().split()


i = 0
while i < len(numbers):
  n = int(numbers[i])
  lista_a.append(n)
  i += 1

m = int(positions[0])
n = int(positions[1])

if m > len(lista_a)-1 or n > len(lista_a)-1 or m < 0 or n < 0:
  print('INVALID')
else:
    if m > n:
        aux = m
        m = n
        n = aux
    i = m 
    soma = 0
    while i <= n:
        soma += lista_a[i]
        i += 1
    print(soma)