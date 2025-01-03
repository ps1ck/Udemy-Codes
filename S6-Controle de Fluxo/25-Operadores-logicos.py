renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil and nome_limpo:     # Aqui posso usar and ou or, no and os dois tem que ser True, no or, no MÍNIMO um.
    print('AND// Financiamento Aprovado!')
else:
    print('AND// Financiamento Negado!')

if renda_acima_5mil or nome_limpo:      # Da pra ir brincando mudando os valores ai
    print('OR // Financiamento Aprovado.')
else:
    print('OR // Financiamento Reprovado.')

# Em vez de mudar manualmente ali eu quero testar se consigo fazer um com input de numero pra renda e fazer uma verificação 
#de strings como se fosse o banco de dados que me informa os nomes limpos.

renda = input('Digite sua renda mensal: ')
nome = input('Digite seu nome:')
nomelimpoEx = 'Rian' #Aqui no caso só tem UM nome limpo, mas aqui poderia ter alguma função que puxa uma lista de nomes
                     # limpos, aqui ta sendo só um exemplo mesmo.
if float(renda) > 5000 and str(nome) == str(nomelimpoEx):
    print('Financiamento Aprovado!')
else:
    print('Financiamento Reprovado!')

#FUNCIONA! Não tava funcionando antes pq eu tava usando a variável nome_limpo em vez de nomelimpoEx, mas quando vi isso
# deu tudo certo, to evoluindo bem..