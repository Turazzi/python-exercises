#exchanges adjacent values

n = int(input())
numbers = input().split()
list_n = []
list_n2 = []


i = 0
while i < len(numbers):
  n = int(numbers[i])
  list_n.append(n)
  list_n2.append(n)
  i += 1

i = 0
j = 1
while j < len(list_n):
  if i % 2 == 0:
    list_n[i] = list_n2[j]
    list_n[j] = list_n2[i]
  i += 1
  j += 1

i = 0
while i < len(list_n):
  print(list_n[i], end = ' ')
  i += 1
