# print (type(nome da variavel)) --> isso é extremamente útil, se estiver dando um erro por estar somando uma string com um int por exemplo posso usar esse comando pra
# saber qual é qual e corrigir o erro (igual ele fez nessa aula) 
ano_nascimento = input('Em que ano você nasceu: ')
idade = 2024 - int(ano_nascimento)
print(idade)
# sobre a duvida da ultima aula, ainda não sei como filtrar o que o usuário digita, mas pra fazer a conta eu consigo/preciso receber o que ele digitou e transformar em
# inteiro pra que o programa possa executar com tranquilidade o cálculo.

# vou tentar melhorar um pouco esse programa:
'''
só tirar as aspas e colocar no de cima que ele funciona!

nome = input('Qual é o seu nome: ')
anoN = input('Olá '+nome+'! Em que ano você nasceu: ')
anoA = input('Em que ano estamos: ')
res = int(anoA) - int(anoN)
print('Você tem '+str(res)+' anos.')
'''