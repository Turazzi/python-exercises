#greatest common divisor (GCD)

n = int(input())
m = int(input())

i = n
while n % i != 0 or m % i != 0: 
    i -= 1

print(i)