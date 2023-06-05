#Seconds in days, hours, minutes and seconds

seconds = int(input())

day = seconds/86400
day_r = seconds%86400
hour = day_r/3600
hour_r = day_r%3600
minute = hour_r/60
minute_r = hour_r%60
second = minute_r%60

print(f"{day:0.0f} {hour:0.0f} {minute:0.0f} {second:0.0f}")