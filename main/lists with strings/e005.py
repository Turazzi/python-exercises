#anagram

word = input()
word2 = input()

anagrama = True
i = 0
while i < len(word) and anagrama == True:
  word_counter = 0
  word_counter2 = 0
  if word[i] == ' ':
    i += 1
  else:
    j = 0
    for j in range(len(word2)):
      if word[i] == word2[j]:
        word_counter2 += 1
    j = 0
    for j in range(len(word)):
      if word[i] == word[j]:
        word_counter += 1
    i += 1
  if word_counter != word_counter2:
    anagrama = False

if anagrama:
  print(1)
else:
  print(0)