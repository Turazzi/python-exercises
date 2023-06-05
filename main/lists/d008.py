#sum two lists

n = int(input())
numbers = input().split()
numbers2 = input().split()
lista_a = []
lista_b = []


i = 0
while i < len(numbers):
  n = int(numbers[i])
  lista_a.append(n)
  i += 1

i = 0
while i < len(numbers2):
  n = int(numbers2[i])
  lista_b.append(n)
  i += 1

i = 0
lista_c = []
while i < len(lista_a):
  lista_c.append(lista_a[i] + lista_b[i])
  i += 1

i = 0
while i < len(lista_c):
  print(lista_c[i], end = ' ')
  i += 1