# Crie uma função que aceita um número como entrada e retorna o quadrado desse número.
def quadrado(numero):
    return numero * numero

num = int(input('Digite um número: '))
print(f'O quadrado de {num} é {quadrado(num)}')
