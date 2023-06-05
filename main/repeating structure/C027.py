#perfect number
#A number is perfect if ir is equal to the sum of its positive divisors other than N. For example, 6 is perfect, since 1 + 2 + 3 = 6


n = int(input())
i = 1
account = 0


while i < n:
  if n % i == 0:
    account += i

  i+= 1

if account == n:
  print('Y')
else:
  print('N')