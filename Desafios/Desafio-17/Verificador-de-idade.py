# Para este desafio, peça ao usuário para digitar a sua idade. Se a idade for menos que 13, imprima "Você é uma criança". Se
#a idade estiver entre 13 e 19, imprima "Você é um adolescente". Se a idade for 20 ou mais, imprima "Você é um adulto".

idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Você é uma criança')
elif idade >= 13 and idade <= 19:
    print('Você é um adolescente')
elif idade >= 20:
    print('Você é um adulto')