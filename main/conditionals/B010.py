#classification of triangles

a = float(input())
b = float(input())
c = float(input())

invalid1 = a + b
invalid2 = b + c
invalid3 = c + a

if (invalid1 < c) or (invalid2<a) or (invalid3 < b):
    print("INVALID")
if (a!= b != c) and (invalid1 >= c) and (invalid2 >= a) and (invalid3 >= b):
  print("SCALENE")
elif (a==b!=c) or (a!= b == c) or (c == a!= b):
  print("ISOSCELES")
elif a == b == c:
  print("EQUILATERAL")
