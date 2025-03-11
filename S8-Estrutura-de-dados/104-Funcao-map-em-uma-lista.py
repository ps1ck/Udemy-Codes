# Built-in Functions na documentação do python tem várias funções interessantes explicadas
lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2
                                # Map serve pra rodar uma função dentro de uma lista.
lista2 = map(multi, lista1)     # To usando a função multi com os itens da lista1
print(lista2)                   # Ele imprime o "objeto"
print(list(lista2))             # Aqui transofrmamos pra lista pra imprimir os resultados da função em lista.