#speed radar

speed_limit = int(input())
speed_ticket_value = float(input())
additional_value = float(input())
speed = int(input())

if speed > speed_limit:
  speed_ticket = speed_ticket_value + additional_value * (speed - speed_limit)
  print(f"{speed_ticket:0.2f}")
else:
  print("0.00")