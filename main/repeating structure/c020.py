#ages

n = 0
i = -1
soma = 0
age_of_majority = 0
elderly = 0

while n >= 0:
    i += 1
    n = int(input())
    if n >= 18:
        age_of_majority += 1
    if 75 < n:
        elderly += 1
    if n > 0:
        soma += n
    
    

average = (soma / i)

average_elderly = (elderly / i) * 100

print(f"{average:.2f}")
print(age_of_majority)
print(f"{average_elderly:.2f}%")