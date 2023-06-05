#two highest values

n = int(input())
n2 = int(input())
largest = n2
n2 = int(input())
penultimate = n2 

i = 2
while i < n:
    n2 = int(input())
    if n2 > largest and largest > penultimate:
        penultimate = largest
        largest = n2
    elif n2 > largest:
        largest = n2
    elif n2 > penultimate:
        penultimate = n2
    elif largest < penultimate:
        penultimate = penultimate
    i += 1
if penultimate > largest:
    aux = largest
    largest = penultimate
    penultimate = aux
print(largest)
print(penultimate)