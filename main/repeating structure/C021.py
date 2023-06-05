#sum of digits

n = int(input())
soma = 0
t = 0
t2 = 0

while n > 0:
  t = n % 10
  t2 = n // 10
  n = t2
  soma += t

print(soma)