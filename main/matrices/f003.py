#sum of the matrix columns

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

columns_sum = [0] * n_columns

for linha in mat:
  for j in range(n_columns):
    columns_sum[j] = int(columns_sum[j]) + int(linha[j])

for soma in columns_sum:
  print(soma)
