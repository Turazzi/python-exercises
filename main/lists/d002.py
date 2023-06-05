#write list

n = int(input())
m = input().split()
lista_n = []

i = 0
while i < len(m):
  numbers = int(m[i])
  lista_n.append(numbers)
  i += 1

i = 0
while i < len(lista_n):
  print(lista_n[i], end = ' ')
  i += 1