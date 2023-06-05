#maximun increasing segment

n = int(input())
i = 1
m = int(input())
smaller = m 
j = 1
save = 1

while i < n:
    m = int(input())
    if m >= smaller:
        smaller = m 
        j += 1
        if j > save:
            save = j  
    else:
        smaller = m
        j = 1
    i += 1

print(save)

