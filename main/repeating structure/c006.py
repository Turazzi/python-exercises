#harmonic number

n = int(input())
i = 1
h = 0

while i <= n and n > 0:
    h = h + 1 / i
    i += 1

print(f"{h :0.4f}")