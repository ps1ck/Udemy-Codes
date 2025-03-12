from sys import getsizeof

numeros = [x * 10 for x in range(100)]      # List Comprehension, gasta absurdamente mais memória por que ele armazena e depois imprime.
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))                   # Quanto mais itens, mais bytes são usados... Em quantidades enormes isso pode pesar bastante.

print()

numeros = (x * 10 for x in range(100))      # Generator, ele imprime em forma de lista só se for especificado, ele é por default um objeto e não armazena os valores na memória.
print(type(numeros))
print(numeros)                              # Aqui podemos observar que ele imprime somente o objeto
print(list(numeros))                        # Dessa maneira sai os números de fato.
print(getsizeof(numeros))                   # Muito interessante que independente do TAMANHO, ele tende a manter sempre em um valor (nesse caso 200 bytes de memória) muito 
                                            #eficiente em números ENORMES.
                                            