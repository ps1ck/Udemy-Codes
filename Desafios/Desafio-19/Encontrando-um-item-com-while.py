resposta = input('Digite o nome de uma fruta: ')

while resposta.lower() != 'abacate':
    resposta = input('Fruta errada! Digite outra: ')        # O meu código da um retorno quando a pessoa erra, o dele não. Tirando isso, tudo igual!

print('Parabéns, você acertou a fruta!')