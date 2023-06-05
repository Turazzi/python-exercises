#sequence from x to y

x = int(input())
y = int(input())

if x > y:
  print("INVALID")

i = x

while i <= y:
  print(i)
  i = i + 1