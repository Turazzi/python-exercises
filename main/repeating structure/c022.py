#kangoroo

x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())


aux = 0
aux2 = 0

if x1 > x2: 
  aux = x2
  x2 = x1
  x1 = aux

  aux2 = v2
  v2 = v1
  v1 = aux2
if v2 > v1:
  print('NAO')
else:
  i1 = x1
  i2 = x2
  while i1 < i2:
    i1 += v1
    i2 += v2

  if i1 == i2:
    print('YES')
  else:
    print('NO')