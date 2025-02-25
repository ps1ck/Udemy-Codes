aluno = {
        'nome': 'Ana',
        'idade': 16,
        'nota_final': 8.6,
        'aprovação': True,
        'Materias:' : ['Fisica', 'Matematica', 'Ingles']
        }

print(aluno)                    # Mostrando como a lista fica no dicionário
print(aluno.get('Materias'))    # Da pra fazer listas dentro do dicionário, e da pra imprimir a lista pela key.
print(len(aluno))               # Length vai imprimir a quantidade de KEYS, que nesse caso é 5.
print()
print(aluno.items())    # Da pra imprimir cada item específico, ele ainda escreve no console que é de um dict (dictionary).
print(aluno.keys())
print(aluno.values())
