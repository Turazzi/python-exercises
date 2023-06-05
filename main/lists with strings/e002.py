#printing characters of a word in reverse order

n = input()

i = len(n) - 1
while i >= 0:
    print(n[i], end = ' ')
    i -= 1