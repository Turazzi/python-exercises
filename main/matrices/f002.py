#sum of the matrix rows

n = input().split()
n_lines = int(n[0])
n_columns = int(n[1])

mat = []
elements = input().split()

for i in range(n_lines):
  linhas = []
  for j in range(n_columns):
    linhas.append(elements[i * n_columns + j])
  mat.append(linhas)

for linha in mat:
  soma = 0
  for elem in linha:
    soma += int(elem)
  print(soma)    