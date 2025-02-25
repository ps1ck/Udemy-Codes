aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 8.6, 'aprovação': True}

for x in aluno.keys():  # Só as chaves
    print(x)

print()
for x in aluno.values(): # Só os valores
    print(x)

print()
for x in aluno.items(): # Chaves e valores, só que impressos em tuple..
    print(x)

print()
for keys, val in aluno.items():  # Criando duas variáveis ele tira de tuple e imprime bonitinho
    print(keys, val)

# Deixando formatado (teste próprio)
print()
for keys, val in aluno.items():  
    print(f'{keys} -> {val}')       # Funciona certinho
