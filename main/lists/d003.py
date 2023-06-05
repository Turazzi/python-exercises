#higher value and position

n = int(input())
numbers = input().split()
lista_n = []

i = 0
while i < len(numbers):
  num = int(numbers[i])
  lista_n.append(num)
  i += 1

i = 0
largest = lista_n[0]
while i < len(lista_n):
  if lista_n[i] > largest:
    largest = lista_n[i]
  i += 1

i = 0
position = 0
while i < len(lista_n):
  if largest == lista_n[i]:
    position = i
    break
  i += 1

print(largest)
print(position)