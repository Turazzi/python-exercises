#percentage of votes

voters = int(input())
whites = int(input())
nulls = int(input())
valid = int(input())

absent = voters - (whites + nulls + valid)

N = (nulls/voters)*100
W = (whites/voters)*100
V = (valid/voters)*100
A = (absent/voters)*100

print(f"nulls: {N:0.2f}%")
print(f"whites: {W:0.2f}%")
print(f"valid: {V:0.2f}%")
print(f"absent: {A:0.2f}%")