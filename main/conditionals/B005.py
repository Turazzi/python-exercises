#leap year

x = int(input())

if (x / 400) and (x % 400 == 0):
  print('leap year')

elif (x / 4) and (x % 4 == 0):
  if (x / 100) and (x % 100 == 0):
    print('normal year')
  else:
    print('leap year')

elif x <= 0:
  print("invalid")
else:
  print('normal year')