#chocolate

n = int(input()) #money that I have
c = int(input()) #cost of each chocolate
m = int(input()) #discount

choc = n // c
bonus = choc

while bonus >= m:
    choc = choc + (bonus // m) #add up the amount of chocolates you will earn
    bonus = bonus // m + bonus % m

print(choc)
