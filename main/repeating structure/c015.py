#prime number

n = int(input())

if n > 1:
    i = 2
    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1
    else:
        print(1)
else:
    print(0)
