#real roots of a second degree equation

import math

a = float(input())
b = float(input())
c = float(input())

x1 = (b*-1 + math.sqrt(b**2 - 4 * a * c))/(2*a)
x2 = (b*-1 - math.sqrt(b**2 - 4 * a * c))/(2*a)

print(f"{x1:0.2f}")
print(f"{x2:0.2f}")