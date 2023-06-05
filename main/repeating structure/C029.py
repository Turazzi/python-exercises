#palindrome number

n = int(input())
m = n
i = 0
j = 1
k = 1

while k > 0:
    j = m % 10
    i = i * 10 + j
    k = m // 10
    m = k

if i == n:
    print('Y')
else:
    print('N')