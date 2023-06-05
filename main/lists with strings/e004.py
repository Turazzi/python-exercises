#palindrome

palin = input()

i = 0 
j = len(palin) - 1
palindrome = True
while i < len(palin) and palindrome == True:
    if palin[i] == ' ':
      i += 1
    if palin[j] == ' ':
      j -= 1
    if  palin[i] != palin[j]:
        palindrome = False
    i += 1
    j -= 1

if palindrome:
  print(1)
else:
  print(0)