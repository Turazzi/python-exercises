#voters

age = int(input())

if age >= 16 and age <= 17:
  print("Optional voter")
elif age >= 18 and age <=69:
  print("Mandatory voter")
else:
  print("Exempt voter")