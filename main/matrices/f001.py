#prints matrices

n = input().split()
n_lines = int(n[0])
n_columns = int(n[1])

mat = []
elementos = input().split()

for i in range(n_lines):
  linhas = []
  for j in range(n_columns):
    linhas.append(elementos[i * n_columns + j])
  mat.append(linhas)

for i in range(len(mat)):
  for j in range(len(mat[i])):
    print(mat[i][j], end = ' ')
  print()