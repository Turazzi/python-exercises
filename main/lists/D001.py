#above-average temperatures

temperature = input().split()
lista_t = []

i = 0
while i < len(temperature):
  t = int(temperature[i])
  lista_t.append(t)
  i += 1

i = 0
soma = 0
while i < len(lista_t):
  soma += lista_t[i]
  i += 1

media = soma / 7

i = 0
largest = 0
while i < len(lista_t):
  if lista_t[i] > media:
    largest += 1
  i += 1

print(largest)