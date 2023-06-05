#Ana´s number
#If a number non-negative integer N is the product of three consecutive integers, then N is an "Ana´s number"

n = int(input())
i = 1
account = 0

while account < n:
  i += 1
  account = i * (i + 1) * (i + 2)
if account == n:
  print('Y')
else:
    print('N')

