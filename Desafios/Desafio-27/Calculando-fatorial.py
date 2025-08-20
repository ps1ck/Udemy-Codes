# As funções recursivas são funções que se chama dentro do seu próprio bloco de código. Elas são úteis para
#resolver problemas que podem ser divididos em problemas menores de natureza semelhante.
# Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial de um número. O fatorial de um número
#n é o produto de todos os números inteiros positivos de n até 1. 

'''def fatorial(n): --> Função não recursiva (iterativa)
    fat = n
    if n == 1 or n == 0:
        return 1
    else:
        for i in range(n-1, 1, -1):
            fat *= i
        
        return fat'''

def fatorial(n):        # Versão recursiva!
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite o número: "))
print(f'O fatorial de {numero} é {fatorial(numero)}')