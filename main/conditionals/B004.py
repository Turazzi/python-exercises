#Uber ride price

distance_stipulated = float(input()) #viagens até
value1 = float(input())
value2 = float(input())
distance_over_stipulated = float(input()) #km da viagem

if distance_over_stipulated <= distance_stipulated:
  trip = distance_over_stipulated * value1
  print(f"{trip:0.2f}")
else:
  trip2 = distance_over_stipulated * value2
  print(f"{trip2:0.2f}")