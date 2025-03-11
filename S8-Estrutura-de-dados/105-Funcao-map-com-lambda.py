'''
lista1 = [1, 2, 3, 4]
def multi(x):
   return x * 2

lista2 = map(multi, lista1)     
print(lista2)                  
print(list(lista2))'
'''
# UMA MANEIRA MELHOR DE FAZER:
lista = [1, 2, 3, 4]
print(list(map(lambda x: x*2, lista)))  # Coloquei uma função lambda no lugar da função normal, já coloquei dentro do list() pra não ter que criar uma variável, menos linhas,
                                        #mais rápido e fácil de entender. Entendi melhor como se usa o Lambda