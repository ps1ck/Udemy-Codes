idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Você é uma criança')
elif idade >= 13 and idade <= 19:
    print('Você é um adolescente')
elif idade >= 20:
    print('Você é um adulto')