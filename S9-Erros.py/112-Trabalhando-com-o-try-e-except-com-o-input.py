try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:                                          # Um erro diferente do exemplo anterior, agora é valor errado.
    print('Favor digitar um valor em números')

print('Mais código abaixo')                                 # Teste pra entender que ele continua executando tudo a baixo dps do except, diferente do erro que para o programa.