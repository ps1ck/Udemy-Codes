set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) # Mesma coisa que "set1 | set2", junta as duas sem colocar os repetidos
print(set4)
set4 = set1.difference(set3) # Mesma coisa que "set1 - set2", imprime tudo que tem no "set1" e não tem no "set2"
print(set4)
set4 = set1.intersection(set2) # Mesma coisa que "set1 & set2", imprime só o que se repete
print(set4)
set4 = set1.symmetric_difference(set3) # Mesma coisa que "set1 ^ set2", imprime tudo menos o que se repete em ambas ('c' aqui)
print(set4)

# TESTE PRÓPRIO (fora da aula):
print()
setx = set2.union(set3)
print(setx)
sety = setx.intersection(set1) 
print(sety)                     # Juntando o set2 e 3 na váriavel setx e vendo o que se repete nela com o set1, temos esse 
                                #resultado: {'c', 'a'}. Exatamente o proposto.


# OUTRO TESTE PRÓPRIO: 
print()
x = {'mustang', 'ferrari', 'porsche'}
y = {'mclaren', 'astonMartin', 'chevrolet', 'mustang'}

teste = x.union(y)
print(teste)
teste2 = x.intersection(y)
print(teste2)                   # Funciona com textos grandes também, da pra adicionar e ver os repetidos.