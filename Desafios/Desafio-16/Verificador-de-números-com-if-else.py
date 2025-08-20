# Para este desafio, quero que você peça ao usuário que digite um número. Se o número for maior que 10, imprima
#"O número é maior que 10". Caso contrário, imprima "O número é menor ou igual a 10".

number = float(input('Digite um número: '))

if number > 10:
    print('O número é maior que 10')
elif number <= 10:
    print('O número é menor ou igual a 10')