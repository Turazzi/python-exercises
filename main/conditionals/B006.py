#sum of the roots of a second-degree equation

import math

a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c

if delta <= 0:
  print(math.nan)

else:
  x1 = (b*-1 + math.sqrt(delta))/(2*a)
  x2 = (b*-1 - math.sqrt(delta))/(2*a)
  sum = round(x1+x2)

  print(f"{sum:0.2f}")