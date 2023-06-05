#sort tho numbers

a = int(input())
b = int(input())

if a > b:
  aux = b
  b = a
  a = aux

print(a)
print(b)