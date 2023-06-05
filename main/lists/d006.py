#write list in reverse order

n = int(input())
numbers = input().split()
lista_n = []

i = 0
while i < len(numbers):
  n = numbers[i]
  lista_n.append(n)
  i += 1

i = 0
reverse_list = []
while i < len(lista_n):
  n = numbers[i]
  reverse_list.append(n)
  i += 1

i = 0
j = len(lista_n) - 1
while i < len(lista_n):
  reverse_list[i] = lista_n [j]
  i += 1
  j -= 1

i = 0
while i < len(reverse_list):
  print(reverse_list[i], end = ' ')
  i += 1