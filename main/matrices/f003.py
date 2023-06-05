n = input().split()
n_linhas = int(n[0])
n_colunas = int(n[1])

mat = []
elementos = input().split()

for i in range(n_linhas):
  linhas = []
  for j in range(n_colunas):
    linhas.append(elementos[i * n_colunas + j])
  mat.append(linhas)

soma_colunas = [0] * n_colunas

for linha in mat:
  for j in range(n_colunas):
    soma_colunas[j] = int(soma_colunas[j]) + int(linha[j])

for soma in soma_colunas:
  print(soma)