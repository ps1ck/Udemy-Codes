# Sets (Listas)
    # Similar a listas
    # Evite itens duplicados
    # Náo utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

# Funções que posso usar com sets:
print(num1 | num2) # Union - Une as duas listas sem repetir os números (printa só uma vez cada)

print(num1 - num2) # Difference - Imprime tudo que tem na "num1" e não tem na "num2", a diferença.
print(num2 - num1) # Difference - Agora ao contrário, o que tem de diferente na "num2".

print(num1 ^ num2) # Symmetric Difference - Imprime tudo menos o que se repete em ambas.

print(num1 & num2) # And - Imprime só o que se repete em ambas.

print(len(num1)) # Posso usar length (pra saber quantos itens tem no set), mas não posso usar index por exemplo:
# print(num1[0]) - Porque sets não tem index. TypeError: 'set' object is not subscriptable

# Basicamente set serve pra trabalhar com números duplicados, repetidos e etc. Em listas grandes ele pode poupar tempo com
#essas funções de itens duplicados e etc.