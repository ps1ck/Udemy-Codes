# Para este desafio, crie uma função lambda que aceite um número e retorne "Par" se o número for par e "Ímpar"
#se o número for ímpar.

parOUimpar = lambda x: x%2 == 0

numero = int(input("Digite um número para verificação: "))
if parOUimpar(numero):
    print("Par")
else:
    print("Ímpar")

'''
    Também tem essa forma de escrever (vista na solução):
par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Impar'
    Apesar de o meu também funcionar, é mais simples do jeito da solução, mas ta valendo!
'''