#sort three numbers

a = int(input())
b = int(input())
c = int(input())

if a > b and b > c:
    aux = c
    c = a
    a = aux
elif c > b:
    aux = a
    a = b
    b = c
    c = aux
if a < b and b > c:
    aux = b
    b = c 
    c = aux
if a < b and c < a:
    aux = a
    a = c
    c = b
    b = aux
if a > b and b < c:
    aux = a
    a = b
    b = aux

print (a)
print (b)
print (c)