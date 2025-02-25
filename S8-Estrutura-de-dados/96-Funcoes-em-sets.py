tuple = (1, 2, 3, 4, 5, 6)     # Tuples sempre com ()
list = [1, 2, 3, 4, 5, 6]      # Listas sempre com []
s1 = {1, 2, 3, 4, 5, 6}        # Criando um set "diretamente", em vez de "s1 = set([1, 2, 3, 5, 6])"

# Na aula ele comentou que não posso criar um set vazio assim: "s1 = {}" porque isso seria um dicionário vazio, ainda não sei o
#que é um dicionário, mas será assunto de outras aulas.

print(type(tuple))
print(type(list))
print(type(s1))

print(s1)
s1.add(7)                   # Adicionei um número   
print(s1)
s1.add(4)                   # Adicionei um número REPETIDO
print(s1)                   # Como o número é repetido, ele não colocou.
s1.update([8, 9, 10])       # Adiciona vários números de uma vez só (repare que tem que estar dentro de uma lista).
print(s1)                   
s1.update([1, 4, 6, 11])    # Adicionei 3 números repetidos e um número novo.
print(s1)                   # Ele só adiciona o número novo.
s1.remove(11)               # Remove um item
print(s1)

s1.discard(90)              # Discard pode remover um número que NÃO existe na lista, já o remove são apenas os que ESTÃO
# s1.remove(90)             #na lista, o código dessa linha por exemplo daria erro.
print(s1)
