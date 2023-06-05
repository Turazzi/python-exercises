#Fibonacci Sequence

n = int(input())
last = 0
penultime = 1
soma = 1
i = 0
while i < n:
    print(soma)
    soma = penultime + last
    last =  penultime
    penultime = soma
    i += 1