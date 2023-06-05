#sequences x to y and y to x

x = int(input())
y = int(input())

if x > y:
  print("INVALID")
else:
  i = x
  while i <= y:
    print(i)
    i = i + 1
  
  i = y
  while  i >= x:
    print(i)
    i = i - 1