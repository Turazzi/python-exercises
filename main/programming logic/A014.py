#inverts four-digit number

x = int(input())

rest1 = x%10
leftover1 = x//10
rest2 = leftover1%10
leftover2 = leftover1//10
rest3 = leftover2%10
leftover3 = leftover2//10

print(rest1, end="")
print(rest2, end="")
print(rest3, end="")
print(leftover3, end="")