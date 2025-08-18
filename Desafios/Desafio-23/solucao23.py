friends1 = {'Marcos', 'Ana', 'Sophia', 'Arthur', 'Amanda'}
friends2 = {'Jose', 'Arthur', 'Ana', 'Carol', 'Paulo'}

result = friends1.intersection(friends2) # Junta o que se repete das listas (objetivo desse desafio)
# # result = friends1.union(friends2)   # Une os dois sets sem repetir os nomes (sem coloca-los 2x)
# result = friends1.difference(friends2)    # Pega a diferença, tudo que tem em friends1 e não tem no friends2
print(result)