# Para este desafio, crie duas funções. A primeira função deve aceitar um número e retornar o dobro desse número.
#A segunda função deve aceitar um número e retornar o quadrado desse número. Em seguida, chame a primeira função 
#dentro da segunda para retornar o quadrado do dobro de um número.

def dobro(numero):
    return numero * 2

def quadrado(numero):
    return numero * numero

user_number = int(input("Digite um número: "))

print(f'O dobro de {user_number} é: {dobro(user_number)}')
print(f'O quadrado de {user_number} é: {quadrado(user_number)}')
print(f'O quadrado do dobro de {user_number} é: {quadrado(dobro(user_number))}')