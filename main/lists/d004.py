#search number

n = int(input())
numbers = input().split()
lista_n = []
x = int(input())

i = 0
while i < len(numbers):
  n = int(numbers[i])
  lista_n.append(n)
  i += 1

i = 0
position = 0
while i < len(lista_n):
  if x == lista_n[i]:
    position = i
    break
  else:
    position = -1

  i += 1

print(position)