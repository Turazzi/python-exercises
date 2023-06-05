#counting occurences of a character in a string

word = input()
x = input()

i = 0
j = 0
while i < len(word):
    if word[i] == x:
        j += 1
    i += 1

print(j)